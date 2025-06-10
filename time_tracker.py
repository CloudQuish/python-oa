"""
Time Tracking Utility for Python Assessment
This helps track how long students spend on each question category.
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
import os


class AssessmentTimeTracker:
    """
    Tracks time spent on different parts of the assessment.
    Automatically logs work sessions and generates analytics.
    """
    
    def __init__(self, student_id=None):
        self.student_id = student_id or os.getenv('GITHUB_USER', 'anonymous')
        self.log_file = Path('.assessment_time_log.json')
        self.session_start = None
        self.current_category = None
        self.load_existing_data()
    
    def load_existing_data(self):
        """Load existing time tracking data"""
        if self.log_file.exists():
            with open(self.log_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                'student_id': self.student_id,
                'assignment_start': datetime.now().isoformat(),
                'sessions': [],
                'category_time': {
                    'basic_python': 0,
                    'intermediate_python': 0,
                    'advanced_python': 0,
                    'backend_development': 0,
                    'setup_debugging': 0
                },
                'total_active_time': 0,
                'submission_count': 0
            }
    
    def start_session(self, category='general'):
        """Start tracking a work session"""
        self.session_start = time.time()
        self.current_category = category
        print(f"⏱️  Started tracking time for: {category}")
        print(f"   Current session started at: {datetime.now().strftime('%H:%M:%S')}")
    
    def end_session(self):
        """End current tracking session"""
        if self.session_start is None:
            print("⚠️  No active session to end")
            return
        
        session_duration = time.time() - self.session_start
        session_minutes = session_duration / 60
        
        # Log the session
        session_data = {
            'category': self.current_category,
            'start_time': datetime.fromtimestamp(self.session_start).isoformat(),
            'end_time': datetime.now().isoformat(),
            'duration_minutes': round(session_minutes, 2)
        }
        
        self.data['sessions'].append(session_data)
        self.data['category_time'][self.current_category] += session_minutes
        self.data['total_active_time'] += session_minutes
        
        print(f"⏹️  Session ended: {round(session_minutes, 1)} minutes on {self.current_category}")
        
        self.save_data()
        self.session_start = None
        self.current_category = None
    
    def log_submission(self):
        """Log when student submits (pushes to GitHub)"""
        self.data['submission_count'] += 1
        self.data['last_submission'] = datetime.now().isoformat()
        self.save_data()
        print(f"📤 Submission #{self.data['submission_count']} logged")
    
    def save_data(self):
        """Save tracking data to file"""
        with open(self.log_file, 'w') as f:
            json.dump(self.data, indent=2, fp=f)
    
    def get_summary(self):
        """Generate time tracking summary"""
        total_time = self.data['total_active_time']
        
        summary = f"""
🕒 Assessment Time Summary for {self.data['student_id']}
{'=' * 50}

📊 Time by Category:
• Basic Python (Q1-Q5):        {self.data['category_time']['basic_python']:.1f} min
• Intermediate Python (Q6-Q10): {self.data['category_time']['intermediate_python']:.1f} min  
• Advanced Python (Q11-Q15):    {self.data['category_time']['advanced_python']:.1f} min
• Backend Development (Q16-Q20): {self.data['category_time']['backend_development']:.1f} min
• Setup & Debugging:            {self.data['category_time']['setup_debugging']:.1f} min

⏱️  Total Active Time: {total_time:.1f} minutes ({total_time/60:.1f} hours)
📤 Total Submissions: {self.data['submission_count']}
📅 Started: {self.data['assignment_start'][:19].replace('T', ' ')}

🎯 Efficiency Metrics:
• Average time per question: {total_time/20:.1f} minutes
• Time per point: {total_time/100:.1f} minutes
• Sessions: {len(self.data['sessions'])}
"""
        return summary
    
    def export_analytics(self):
        """Export detailed analytics for instructor review"""
        analytics_file = f"analytics_{self.student_id}_{datetime.now().strftime('%Y%m%d')}.json"
        
        analytics_data = {
            **self.data,
            'completion_rate': self.estimate_completion_rate(),
            'efficiency_score': self.calculate_efficiency_score(),
            'time_distribution': self.get_time_distribution()
        }
        
        with open(analytics_file, 'w') as f:
            json.dump(analytics_data, indent=2, fp=f)
        
        print(f"📊 Analytics exported to: {analytics_file}")
        return analytics_file
    
    def estimate_completion_rate(self):
        """Estimate how much of the assessment is completed based on time distribution"""
        total_time = self.data['total_active_time']
        if total_time < 30:  # Less than 30 minutes
            return "Getting Started (0-25%)"
        elif total_time < 90:  # 30-90 minutes
            return "In Progress (25-50%)"
        elif total_time < 150:  # 90-150 minutes
            return "Substantial Progress (50-75%)"
        elif total_time < 240:  # 150-240 minutes (4 hours)
            return "Nearly Complete (75-100%)"
        else:
            return "Extended Work (100%+)"
    
    def calculate_efficiency_score(self):
        """Calculate efficiency based on time distribution"""
        category_times = self.data['category_time']
        total_time = sum(category_times.values())
        
        if total_time == 0:
            return 0
        
        # Ideal time distribution (based on point weights)
        ideal_distribution = {
            'basic_python': 0.20,      # 20 points = 20%
            'intermediate_python': 0.25,  # 25 points = 25%
            'advanced_python': 0.30,   # 30 points = 30%
            'backend_development': 0.25  # 25 points = 25%
        }
        
        # Calculate actual distribution
        actual_distribution = {
            category: time_spent / total_time 
            for category, time_spent in category_times.items()
            if category != 'setup_debugging'
        }
        
        # Calculate efficiency (lower deviation = higher efficiency)
        deviation = sum(
            abs(actual_distribution.get(cat, 0) - ideal_distribution[cat])
            for cat in ideal_distribution
        )
        
        efficiency = max(0, 100 - (deviation * 100))
        return round(efficiency, 1)
    
    def get_time_distribution(self):
        """Get percentage time distribution"""
        total_time = self.data['total_active_time']
        if total_time == 0:
            return {}
        
        return {
            category: round((time_spent / total_time) * 100, 1)
            for category, time_spent in self.data['category_time'].items()
        }


# Global tracker instance
tracker = AssessmentTimeTracker()

# Convenience functions for easy use
def start_basic_python():
    """Start timing Basic Python questions (Q1-Q5)"""
    tracker.start_session('basic_python')

def start_intermediate_python():
    """Start timing Intermediate Python questions (Q6-Q10)"""
    tracker.start_session('intermediate_python')

def start_advanced_python():
    """Start timing Advanced Python questions (Q11-Q15)"""
    tracker.start_session('advanced_python')

def start_backend_development():
    """Start timing Backend Development questions (Q16-Q20)"""
    tracker.start_session('backend_development')

def start_setup_debugging():
    """Start timing setup or debugging activities"""
    tracker.start_session('setup_debugging')

def end_session():
    """End current timing session"""
    tracker.end_session()

def log_submission():
    """Log a submission (call this before git push)"""
    tracker.log_submission()

def show_summary():
    """Show time tracking summary"""
    print(tracker.get_summary())

def export_data():
    """Export analytics data for instructor"""
    return tracker.export_analytics()


if __name__ == "__main__":
    # Command line interface
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python time_tracker.py [start_basic|start_intermediate|start_advanced|start_backend|start_setup|end|submit|summary|export]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'start_basic':
        start_basic_python()
    elif command == 'start_intermediate':
        start_intermediate_python()
    elif command == 'start_advanced':
        start_advanced_python()
    elif command == 'start_backend':
        start_backend_development()
    elif command == 'start_setup':
        start_setup_debugging()
    elif command == 'end':
        end_session()
    elif command == 'submit':
        log_submission()
    elif command == 'summary':
        show_summary()
    elif command == 'export':
        export_data()
    else:
        print(f"Unknown command: {command}") 