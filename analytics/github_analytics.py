"""
GitHub Analytics for Python Assessment
Collects comprehensive time and performance data from GitHub repositories.
"""

import requests
import json
import csv
from datetime import datetime, timedelta
import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


class GitHubAnalytics:
    """
    Collects and analyzes data from GitHub Classroom repositories.
    Requires GitHub token with repo access.
    """
    
    def __init__(self, github_token, organization, assignment_prefix="python-backend-assessment"):
        self.token = github_token
        self.org = organization
        self.assignment_prefix = assignment_prefix
        self.headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.students_data = []
    
    def get_assignment_repositories(self):
        """Get all repositories for this assignment"""
        url = f"https://api.github.com/orgs/{self.org}/repos"
        repos = []
        page = 1
        
        while True:
            response = requests.get(
                url,
                headers=self.headers,
                params={'page': page, 'per_page': 100}
            )
            
            if response.status_code != 200:
                print(f"Error fetching repos: {response.status_code}")
                break
            
            page_repos = response.json()
            if not page_repos:
                break
            
            # Filter for assignment repos
            assignment_repos = [
                repo for repo in page_repos
                if repo['name'].startswith(self.assignment_prefix)
            ]
            repos.extend(assignment_repos)
            page += 1
        
        print(f"Found {len(repos)} assignment repositories")
        return repos
    
    def analyze_repository(self, repo):
        """Analyze a single student repository"""
        repo_name = repo['name']
        student_username = repo_name.replace(f"{self.assignment_prefix}-", "")
        
        print(f"Analyzing {student_username}...")
        
        # Get commit history
        commits = self.get_commits(repo_name)
        
        # Get repository creation time (assignment acceptance)
        created_at = datetime.fromisoformat(repo['created_at'].replace('Z', '+00:00'))
        
        # Calculate metrics
        analysis = {
            'student_username': student_username,
            'repo_name': repo_name,
            'assignment_accepted': created_at,
            'total_commits': len(commits),
            'first_commit': None,
            'last_commit': None,
            'total_time_span': None,
            'active_coding_time': None,
            'commit_frequency': [],
            'late_night_commits': 0,
            'weekend_commits': 0,
            'commit_sizes': [],
            'test_pass_progression': [],
            'estimated_active_time': None
        }
        
        if commits:
            # Sort commits chronologically
            commits.sort(key=lambda x: x['commit']['author']['date'])
            
            first_commit_time = datetime.fromisoformat(
                commits[0]['commit']['author']['date'].replace('Z', '+00:00')
            )
            last_commit_time = datetime.fromisoformat(
                commits[-1]['commit']['author']['date'].replace('Z', '+00:00')
            )
            
            analysis['first_commit'] = first_commit_time
            analysis['last_commit'] = last_commit_time
            analysis['total_time_span'] = (last_commit_time - first_commit_time).total_seconds() / 3600  # hours
            
            # Analyze commit patterns
            analysis.update(self.analyze_commit_patterns(commits))
            
            # Estimate active coding time
            analysis['estimated_active_time'] = self.estimate_active_time(commits)
        
        # Get test results from GitHub Actions
        analysis['test_results'] = self.get_test_results(repo_name)
        
        # Look for time tracking data
        analysis['time_tracking_data'] = self.get_time_tracking_data(repo_name)
        
        return analysis
    
    def get_commits(self, repo_name):
        """Get all commits for a repository"""
        url = f"https://api.github.com/repos/{self.org}/{repo_name}/commits"
        commits = []
        page = 1
        
        while True:
            response = requests.get(
                url,
                headers=self.headers,
                params={'page': page, 'per_page': 100}
            )
            
            if response.status_code != 200:
                break
            
            page_commits = response.json()
            if not page_commits:
                break
            
            commits.extend(page_commits)
            page += 1
        
        return commits
    
    def analyze_commit_patterns(self, commits):
        """Analyze patterns in commit timing and frequency"""
        commit_hours = []
        commit_days = []
        commit_intervals = []
        
        prev_time = None
        
        for commit in commits:
            commit_time = datetime.fromisoformat(
                commit['commit']['author']['date'].replace('Z', '+00:00')
            )
            
            commit_hours.append(commit_time.hour)
            commit_days.append(commit_time.weekday())  # 0 = Monday, 6 = Sunday
            
            if prev_time:
                interval = (commit_time - prev_time).total_seconds() / 60  # minutes
                commit_intervals.append(interval)
            
            prev_time = commit_time
        
        # Count late night commits (11 PM - 6 AM)
        late_night_commits = sum(1 for hour in commit_hours if hour >= 23 or hour <= 6)
        
        # Count weekend commits (Saturday = 5, Sunday = 6)
        weekend_commits = sum(1 for day in commit_days if day >= 5)
        
        return {
            'late_night_commits': late_night_commits,
            'weekend_commits': weekend_commits,
            'commit_hours': commit_hours,
            'commit_intervals': commit_intervals,
            'avg_commit_interval': sum(commit_intervals) / len(commit_intervals) if commit_intervals else 0
        }
    
    def estimate_active_time(self, commits):
        """Estimate active coding time based on commit patterns"""
        if len(commits) < 2:
            return 0
        
        active_sessions = []
        current_session_start = None
        session_threshold_minutes = 120  # 2 hours gap = new session
        
        for i, commit in enumerate(commits):
            commit_time = datetime.fromisoformat(
                commit['commit']['author']['date'].replace('Z', '+00:00')
            )
            
            if i == 0:
                current_session_start = commit_time
                continue
            
            prev_commit_time = datetime.fromisoformat(
                commits[i-1]['commit']['author']['date'].replace('Z', '+00:00')
            )
            
            gap_minutes = (commit_time - prev_commit_time).total_seconds() / 60
            
            if gap_minutes > session_threshold_minutes:
                # End current session, start new one
                if current_session_start:
                    session_duration = (prev_commit_time - current_session_start).total_seconds() / 60
                    active_sessions.append(max(session_duration, 15))  # Minimum 15 min per session
                
                current_session_start = commit_time
        
        # Add final session
        if current_session_start and commits:
            final_time = datetime.fromisoformat(
                commits[-1]['commit']['author']['date'].replace('Z', '+00:00')
            )
            session_duration = (final_time - current_session_start).total_seconds() / 60
            active_sessions.append(max(session_duration, 15))
        
        return sum(active_sessions)  # Total minutes
    
    def get_test_results(self, repo_name):
        """Get GitHub Actions test results"""
        url = f"https://api.github.com/repos/{self.org}/{repo_name}/actions/runs"
        
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                runs = response.json()['workflow_runs']
                
                test_results = []
                for run in runs[:10]:  # Last 10 runs
                    test_results.append({
                        'run_id': run['id'],
                        'status': run['status'],
                        'conclusion': run['conclusion'],
                        'created_at': run['created_at'],
                        'updated_at': run['updated_at']
                    })
                
                return test_results
        except Exception as e:
            print(f"Error getting test results for {repo_name}: {e}")
        
        return []
    
    def get_time_tracking_data(self, repo_name):
        """Get time tracking data if available"""
        url = f"https://api.github.com/repos/{self.org}/{repo_name}/contents/.assessment_time_log.json"
        
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                content = response.json()
                import base64
                tracking_data = json.loads(base64.b64decode(content['content']).decode())
                return tracking_data
        except Exception as e:
            print(f"No time tracking data for {repo_name}: {e}")
        
        return None
    
    def analyze_all_students(self):
        """Analyze all student repositories"""
        repos = self.get_assignment_repositories()
        
        for repo in repos:
            analysis = self.analyze_repository(repo)
            self.students_data.append(analysis)
        
        return self.students_data
    
    def generate_analytics_report(self, output_dir="analytics_output"):
        """Generate comprehensive analytics report"""
        Path(output_dir).mkdir(exist_ok=True)
        
        # Convert to DataFrame for analysis
        df_data = []
        for student in self.students_data:
            row = {
                'student': student['student_username'],
                'total_commits': student['total_commits'],
                'total_time_span_hours': student.get('total_time_span', 0),
                'estimated_active_time_hours': (student.get('estimated_active_time', 0) or 0) / 60,
                'late_night_commits': student['late_night_commits'],
                'weekend_commits': student['weekend_commits'],
                'avg_commit_interval_min': student.get('avg_commit_interval', 0),
                'has_time_tracking': student['time_tracking_data'] is not None
            }
            
            # Add time tracking data if available
            if student['time_tracking_data']:
                tracking = student['time_tracking_data']
                row.update({
                    'tracked_total_time': tracking.get('total_active_time', 0),
                    'tracked_basic_python': tracking.get('category_time', {}).get('basic_python', 0),
                    'tracked_intermediate': tracking.get('category_time', {}).get('intermediate_python', 0),
                    'tracked_advanced': tracking.get('category_time', {}).get('advanced_python', 0),
                    'tracked_backend': tracking.get('category_time', {}).get('backend_development', 0),
                    'submission_count': tracking.get('submission_count', 0)
                })
            
            df_data.append(row)
        
        df = pd.DataFrame(df_data)
        
        # Generate reports
        self.create_summary_report(df, output_dir)
        self.create_visualizations(df, output_dir)
        self.export_detailed_data(output_dir)
        
        print(f"📊 Analytics report generated in {output_dir}/")
    
    def create_summary_report(self, df, output_dir):
        """Create summary statistics report"""
        with open(f"{output_dir}/summary_report.md", 'w') as f:
            f.write("# Python Assessment Analytics Summary\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Total Students:** {len(df)}\n\n")
            
            f.write("## Time Analysis\n")
            f.write(f"- **Average Active Time:** {df['estimated_active_time_hours'].mean():.1f} hours\n")
            f.write(f"- **Median Active Time:** {df['estimated_active_time_hours'].median():.1f} hours\n")
            f.write(f"- **Students with Time Tracking:** {df['has_time_tracking'].sum()}/{len(df)}\n\n")
            
            f.write("## Submission Patterns\n")
            f.write(f"- **Average Commits:** {df['total_commits'].mean():.1f}\n")
            f.write(f"- **Late Night Workers:** {(df['late_night_commits'] > 0).sum()}/{len(df)}\n")
            f.write(f"- **Weekend Workers:** {(df['weekend_commits'] > 0).sum()}/{len(df)}\n\n")
            
            if 'tracked_total_time' in df.columns:
                tracked_df = df[df['has_time_tracking']]
                f.write("## Time Tracking Analysis (Students with Tracking)\n")
                f.write(f"- **Average Total Time:** {tracked_df['tracked_total_time'].mean():.1f} minutes\n")
                f.write(f"- **Time on Basic Python:** {tracked_df['tracked_basic_python'].mean():.1f} minutes\n")
                f.write(f"- **Time on Backend Development:** {tracked_df['tracked_backend'].mean():.1f} minutes\n")
    
    def create_visualizations(self, df, output_dir):
        """Create visualization charts"""
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Time distribution
        axes[0, 0].hist(df['estimated_active_time_hours'], bins=20, alpha=0.7)
        axes[0, 0].set_title('Distribution of Active Time (Hours)')
        axes[0, 0].set_xlabel('Hours')
        axes[0, 0].set_ylabel('Number of Students')
        
        # Commit frequency
        axes[0, 1].hist(df['total_commits'], bins=15, alpha=0.7, color='orange')
        axes[0, 1].set_title('Distribution of Total Commits')
        axes[0, 1].set_xlabel('Number of Commits')
        axes[0, 1].set_ylabel('Number of Students')
        
        # Work patterns
        pattern_data = {
            'Late Night': (df['late_night_commits'] > 0).sum(),
            'Weekend': (df['weekend_commits'] > 0).sum(),
            'Regular Hours': len(df) - (df['late_night_commits'] > 0).sum()
        }
        axes[1, 0].bar(pattern_data.keys(), pattern_data.values())
        axes[1, 0].set_title('Work Patterns')
        axes[1, 0].set_ylabel('Number of Students')
        
        # Time vs Performance (if test data available)
        if 'submission_count' in df.columns:
            axes[1, 1].scatter(df['estimated_active_time_hours'], df['submission_count'], alpha=0.6)
            axes[1, 1].set_title('Time vs Submission Frequency')
            axes[1, 1].set_xlabel('Active Time (Hours)')
            axes[1, 1].set_ylabel('Number of Submissions')
        
        plt.tight_layout()
        plt.savefig(f"{output_dir}/analytics_visualizations.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def export_detailed_data(self, output_dir):
        """Export detailed data to CSV"""
        # Export student summary
        summary_data = []
        for student in self.students_data:
            summary_data.append({
                'Student': student['student_username'],
                'Total_Commits': student['total_commits'],
                'Time_Span_Hours': student.get('total_time_span', 0),
                'Estimated_Active_Hours': (student.get('estimated_active_time', 0) or 0) / 60,
                'Late_Night_Commits': student['late_night_commits'],
                'Weekend_Commits': student['weekend_commits'],
                'First_Commit': student.get('first_commit', ''),
                'Last_Commit': student.get('last_commit', ''),
                'Has_Time_Tracking': student['time_tracking_data'] is not None
            })
        
        df_summary = pd.DataFrame(summary_data)
        df_summary.to_csv(f"{output_dir}/student_summary.csv", index=False)
        
        # Export detailed JSON
        with open(f"{output_dir}/detailed_analytics.json", 'w') as f:
            json.dump(self.students_data, indent=2, fp=f, default=str)
        
        print(f"📄 Data exported to {output_dir}/")


def main():
    """Main function to run analytics"""
    # Configuration
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    ORGANIZATION = os.getenv('GITHUB_ORG', 'your-org-name')
    ASSIGNMENT_PREFIX = os.getenv('ASSIGNMENT_PREFIX', 'python-backend-assessment')
    
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable required")
        print("Create a token at: https://github.com/settings/tokens")
        print("Required scopes: repo, read:org")
        return
    
    # Run analytics
    analytics = GitHubAnalytics(GITHUB_TOKEN, ORGANIZATION, ASSIGNMENT_PREFIX)
    
    print("🔍 Starting analytics collection...")
    analytics.analyze_all_students()
    
    print("📊 Generating report...")
    analytics.generate_analytics_report()
    
    print("✅ Analytics complete!")


if __name__ == "__main__":
    main() 