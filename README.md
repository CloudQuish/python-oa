# Python Backend Developer Assessment

## Overview
This assessment contains 20 progressively difficult questions designed to evaluate Python programming skills and backend development capabilities. Total points: 100.

**✨ NEW: Advanced Time Tracking & Analytics**  
Track student progress, identify learning patterns, and get comprehensive performance insights!

## Structure
- `questions/` - Individual question files
- `tests/` - Automated test cases for each question
- `time_tracker.py` - Optional time tracking utility
- `analytics/` - Instructor analytics tools
- `requirements.txt` - Required dependencies

## Setup for GitHub Classroom

### For Instructors:
1. Fork this repository to your GitHub Classroom organization
2. Set up autograding workflow using the provided test cases
3. Configure point allocation in GitHub Classroom settings
4. **NEW**: Set up analytics tracking (see `INSTRUCTOR_ANALYTICS_GUIDE.md`)

### For Students:
1. Clone the assignment repository
2. Install dependencies: `pip install -r requirements.txt`
3. Complete functions in the `questions/` directory
4. **Optional**: Use time tracker to monitor your progress
5. Run tests locally: `pytest tests/`
6. Push solutions to trigger autograding

## Question Categories & Point Distribution

### Basic Python (Questions 1-5) - 20 points
- Data types and basic operations
- Control structures
- Functions and basic algorithms

### Intermediate Python (Questions 6-10) - 25 points
- Object-oriented programming
- Error handling
- File operations
- Data structures

### Advanced Python (Questions 11-15) - 30 points
- Decorators and context managers
- Generators and iterators
- Concurrency basics
- Advanced data manipulation

### Backend Development (Questions 16-20) - 25 points
- REST API development
- Database operations
- Authentication
- Testing and deployment concepts

## 🕒 Time Tracking Features

### For Students (Optional)
```bash
# Track your coding sessions by category
python time_tracker.py start_basic      # Start timing Basic Python
python time_tracker.py end             # End current session
python time_tracker.py summary         # View time breakdown
```

**Benefits:**
- Learn about your coding patterns
- Identify which topics need more practice
- Track improvement over time
- Get efficiency feedback

### For Instructors (Analytics)
```bash
# Generate comprehensive analytics
cd analytics/
python github_analytics.py
```

**Get insights on:**
- Student time distribution across question categories
- Work patterns (late night, weekend coding)
- Submission frequency and progression
- Class-wide performance statistics
- Academic integrity indicators

## 📊 Analytics Capabilities

### Automatic Tracking (GitHub Classroom)
- Assignment acceptance times
- Commit timestamps and frequency
- Submission patterns
- Repository activity

### Advanced Analytics (GitHub API)
- Estimated active coding time
- Commit pattern analysis
- Work schedule insights
- Performance correlations
- Efficiency metrics

### Generated Reports
- Individual student time summaries
- Class performance overview
- Visual analytics charts
- CSV exports for gradebooks
- Academic integrity flags

## Grading Scale
- 90-100: Excellent
- 80-89: Good
- 70-79: Satisfactory
- 60-69: Needs Improvement
- Below 60: Unsatisfactory

## Time Limit
Recommended time: 3-4 hours

## 📁 Complete File Structure

```
python-backend-assessment/
├── README.md                     # This overview
├── STUDENT_GUIDE.md             # Detailed student instructions
├── INSTRUCTOR_ANALYTICS_GUIDE.md # Analytics setup and usage
├── ASSESSMENT_SUMMARY.md        # Complete question breakdown
├── requirements.txt             # Core dependencies
├── pytest.ini                  # Test configuration
├── time_tracker.py             # Student time tracking tool
│
├── .github/workflows/
│   └── autograding.yml         # GitHub Classroom autograder
│
├── questions/
│   ├── __init__.py
│   ├── basic_python.py         # Questions 1-5 (20 pts)
│   ├── intermediate_python.py  # Questions 6-10 (25 pts)
│   ├── advanced_python.py      # Questions 11-15 (30 pts)
│   └── backend_development.py  # Questions 16-20 (25 pts)
│
├── tests/
│   ├── __init__.py
│   ├── test_basic_python.py
│   ├── test_intermediate_python.py
│   ├── test_advanced_python.py
│   └── test_backend_development.py
│
└── analytics/
    ├── requirements_analytics.txt
    └── github_analytics.py     # Instructor analytics tool
```

## 🚀 Quick Start for Different Users

### Students
1. **Accept assignment** in GitHub Classroom
2. **Clone repository**: `git clone [YOUR_REPO_URL]`
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Start coding**: Begin with `questions/basic_python.py`
5. **Optional tracking**: Use `python time_tracker.py start_basic`
6. **Test often**: `pytest tests/test_basic_python.py -v`
7. **Submit**: `git add . && git commit -m "Progress" && git push`

### Instructors (Setup)
1. **Create template** repository with all assessment files
2. **Set up GitHub Classroom** assignment
3. **Configure autograding** (automatic with included workflow)
4. **Test with sample** submission
5. **Share assignment** link with students

### Instructors (Analytics)
1. **Get GitHub token**: https://github.com/settings/tokens
2. **Set environment variables**:
   ```bash
   export GITHUB_TOKEN="your_token"
   export GITHUB_ORG="your-org-name"
   ```
3. **Install analytics tools**: `pip install -r analytics/requirements_analytics.txt`
4. **Run analytics**: `python analytics/github_analytics.py`
5. **Review reports** in `analytics_output/` directory

## 🎯 Key Features

### ✅ Comprehensive Assessment
- 20 carefully designed questions
- Progressive difficulty
- Real-world backend scenarios
- Complete test coverage

### ✅ Automated Grading
- GitHub Classroom integration
- Instant feedback for students
- Zero manual grading work
- Detailed test results

### ✅ Advanced Analytics
- Time tracking and analysis
- Work pattern insights
- Academic integrity tools
- Performance metrics

### ✅ Educational Value
- Learn about coding patterns
- Identify improvement areas
- Track skill development
- Professional-level scenarios

## 📈 Success Metrics

This assessment system provides insights into:
- **Student Learning**: Time allocation, difficulty patterns, improvement areas
- **Instructor Efficiency**: Automated grading, comprehensive analytics
- **Academic Integrity**: Unusual patterns, collaboration detection
- **Course Improvement**: Question difficulty analysis, time expectations

## 🔧 Customization Options

- Modify point allocations per question
- Add/remove questions based on course focus
- Adjust time limits in autograder
- Customize grading scale
- Add additional test cases
- Configure analytics parameters

Ready to revolutionize your Python assessment experience? 🚀 