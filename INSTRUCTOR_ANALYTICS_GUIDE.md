# Instructor Analytics Guide - Time Tracking & Performance Analysis

## 📊 Overview

This guide shows you how to access comprehensive time tracking and performance analytics for your Python assessment. You can track:

- **Total time spent** by each student
- **Time distribution** across question categories  
- **Work patterns** (late night, weekend coding)
- **Submission frequency** and progression
- **Efficiency metrics** and completion estimates

---

## 🕒 Time Tracking Methods Available

### 1. GitHub Classroom Built-in Analytics (Automatic)

**What you get:**
- Assignment acceptance time
- First and last commit timestamps
- Total number of commits
- Submission times

**How to access:**
1. Go to your GitHub Classroom assignment
2. Click "View assignment" 
3. Click "Download grades" for CSV export
4. Review individual student progress

### 2. Custom Time Tracker (Optional for Students)

**Enhanced tracking includes:**
- Active work sessions by category
- Break time vs active time
- Question-specific time allocation
- Efficiency scoring
- Self-reported time logs

**Student usage:**
```bash
# Students can optionally use the time tracker
python time_tracker.py start_basic      # Start timing Basic Python questions
python time_tracker.py end             # End current session
python time_tracker.py summary         # View time summary
```

### 3. GitHub API Analytics (Advanced)

**Comprehensive analysis:**
- Commit pattern analysis
- Estimated active coding time
- Work schedule patterns
- Performance correlations
- Class-wide statistics

---

## 🚀 Setting Up Analytics

### For Basic Analytics (GitHub Classroom)

No setup required! GitHub Classroom automatically tracks:
- When students accept assignments
- All commit timestamps
- Final submission times

### For Advanced Analytics (GitHub API)

1. **Create GitHub Token:**
   ```bash
   # Go to: https://github.com/settings/tokens
   # Create token with 'repo' and 'read:org' permissions
   export GITHUB_TOKEN="your_token_here"
   export GITHUB_ORG="your-organization-name"
   ```

2. **Install Analytics Dependencies:**
   ```bash
   pip install -r analytics/requirements_analytics.txt
   ```

3. **Run Analytics:**
   ```bash
   cd analytics/
   python github_analytics.py
   ```

### For Student Time Tracking (Optional)

Add `time_tracker.py` to your assignment template:
1. Include `time_tracker.py` in your GitHub Classroom template
2. Instruct students to use it (optional, not graded)
3. Analytics script automatically collects this data

---

## 📈 Understanding the Analytics

### Time Metrics Explained

#### 1. Assignment Span Time
- **What it is:** Time from first commit to last commit
- **What it means:** How long the student worked on the assignment
- **Typical range:** 1-7 days for a 3-4 hour assessment

#### 2. Estimated Active Time  
- **What it is:** Calculated from commit patterns, excluding long gaps
- **Algorithm:** Groups commits into sessions (gaps >2 hours = new session)
- **What it means:** Actual coding time, more accurate than span time
- **Typical range:** 2-6 hours for the full assessment

#### 3. Category Time Distribution
- **Basic Python:** Expected 20% of time (matching 20% of points)
- **Intermediate:** Expected 25% of time  
- **Advanced:** Expected 30% of time
- **Backend:** Expected 25% of time

### Performance Indicators

#### 🟢 Good Patterns
- **Steady commits:** Regular progress over time
- **Balanced distribution:** Time matches point weights
- **Reasonable pace:** 2-4 hours total active time
- **Multiple sessions:** Shows thoughtful approach

#### 🟡 Watch For
- **Very quick completion:** <90 minutes (may indicate shortcuts)
- **Very long time:** >6 hours (may need help)
- **Late night heavy:** >50% commits after 11 PM (burnout risk)
- **Last-minute rush:** >80% of work in final 24 hours

#### 🔴 Red Flags
- **No commits for days, then sudden completion:** Possible collaboration
- **Perfect code with minimal commits:** Possible copying
- **Identical commit patterns:** Compare suspicious submissions

---

## 📊 Sample Analytics Reports

### Class Summary Report Example

```
# Python Assessment Analytics Summary

**Generated:** 2024-01-15 14:30:00
**Total Students:** 25

## Time Analysis
- **Average Active Time:** 3.2 hours
- **Median Active Time:** 2.8 hours  
- **Students with Time Tracking:** 18/25

## Submission Patterns
- **Average Commits:** 12.4
- **Late Night Workers:** 8/25
- **Weekend Workers:** 15/25

## Time Distribution (Students with Tracking)
- **Basic Python:** 45.2 minutes average
- **Backend Development:** 52.1 minutes average
- **Setup & Debugging:** 23.8 minutes average
```

### Individual Student Analysis

```
🕒 Assessment Time Summary for student_username
==================================================

📊 Time by Category:
• Basic Python (Q1-Q5):        38.5 min
• Intermediate Python (Q6-Q10): 67.2 min  
• Advanced Python (Q11-Q15):    89.1 min
• Backend Development (Q16-Q20): 72.3 min
• Setup & Debugging:            15.9 min

⏱️  Total Active Time: 283.0 minutes (4.7 hours)
📤 Total Submissions: 8
📅 Started: 2024-01-12 09:15:00

🎯 Efficiency Metrics:
• Average time per question: 14.2 minutes
• Time per point: 2.8 minutes
• Sessions: 6
• Efficiency Score: 87.3/100
```

---

## 🔧 Running Analytics

### Quick Analytics (GitHub Classroom Export)

1. **Download grades** from GitHub Classroom
2. **Open CSV** in Excel/Google Sheets
3. **Review columns:**
   - `points_awarded` - Final score
   - `github_username` - Student identifier
   - `assignment_url` - Link to student repo
   - `submission_timestamp` - When submitted

### Advanced Analytics (Automated)

```bash
# Set environment variables
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
export GITHUB_ORG="your-classroom-org"
export ASSIGNMENT_PREFIX="python-backend-assessment"

# Run analytics
cd analytics/
python github_analytics.py

# Output generated in analytics_output/:
# - summary_report.md (overview)
# - analytics_visualizations.png (charts)
# - student_summary.csv (spreadsheet data)
# - detailed_analytics.json (raw data)
```

### Custom Queries

```python
# Example: Find students who worked late nights
from analytics.github_analytics import GitHubAnalytics

analytics = GitHubAnalytics(token, org)
analytics.analyze_all_students()

late_night_students = [
    student for student in analytics.students_data 
    if student['late_night_commits'] > 5
]

print(f"Students with >5 late night commits: {len(late_night_students)}")
```

---

## 📋 Using Analytics for Grading

### Academic Integrity

**Time patterns can indicate:**
- Sudden completion after no activity
- Identical submission times across students  
- Unrealistic speed (full completion in <1 hour)
- Perfect code with minimal iteration

**Investigation steps:**
1. Check commit history and timing
2. Compare code similarity between suspicious students
3. Review individual question progression
4. Consider interview for clarification

### Providing Feedback

**Use time data to:**
- Identify students who struggled (>6 hours total)
- Recognize efficient problem solvers (2-3 hours, good results)
- Offer study tips based on time distribution
- Suggest time management improvements

**Example feedback:**
> "I noticed you spent most of your time on Basic Python questions. For future assessments, consider moving through the easier questions more quickly to save time for the advanced concepts where you can earn more points."

### Grade Adjustments

**Consider time factors for:**
- Partial credit decisions
- Extra time accommodations
- Identifying students who need additional support
- Recognizing exceptional efficiency

---

## 🎯 Best Practices for Instructors

### Before Assignment

1. **Test the analytics** with a sample submission
2. **Set clear expectations** about time limits
3. **Explain time tracking** as learning tool (if using)
4. **Prepare intervention** for students taking >6 hours

### During Assignment

1. **Monitor early submissions** for setup issues
2. **Check for students** with no activity after 24 hours
3. **Watch for red flag patterns** in real-time
4. **Offer help** to students struggling >4 hours

### After Assignment

1. **Run full analytics** before final grading
2. **Investigate suspicious patterns** 
3. **Provide personalized feedback** based on time data
4. **Use insights** to improve future assignments

### Privacy Considerations

- **Time tracking is optional** for students
- **Aggregate data only** for research/improvement
- **Protect individual** student timing data
- **Focus on learning** not surveillance

---

## 📊 Analytics Output Examples

### Generated Files

1. **`summary_report.md`** - Class overview statistics
2. **`analytics_visualizations.png`** - Charts and graphs
3. **`student_summary.csv`** - Spreadsheet for gradebook
4. **`detailed_analytics.json`** - Complete raw data

### Visualization Examples

- **Time Distribution Histogram:** Shows spread of student completion times
- **Commit Frequency Chart:** Reveals submission patterns  
- **Work Pattern Analysis:** Late night vs regular hours
- **Time vs Performance Scatter:** Correlation between time and scores

This comprehensive analytics system helps you understand not just *what* students achieved, but *how* they approached the learning process! 