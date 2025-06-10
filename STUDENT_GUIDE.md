# Student Guide - Python Backend Assessment

## 🚀 Quick Start

1. **Clone your assignment repository**
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Complete functions in `questions/` directory**
4. **Test locally**: `pytest tests/`
5. **Push to GitHub for automatic grading**

## 🔧 Troubleshooting Installation

### Python 3.13 Compatibility Issue
If you get pandas/numpy installation errors with Python 3.13:

**Solution 1: Use Core Requirements (Recommended)**
```bash
pip install -r requirements.txt
```
*Note: We've removed pandas/numpy from core requirements for Python 3.13 compatibility*

**Solution 2: If Still Having Issues**
```bash
pip install -r requirements_python313.txt
```

**Solution 3: Use Python 3.11 or 3.12**
```bash
# Create new environment with compatible Python version
conda create -n assessment python=3.11
conda activate assessment
pip install -r requirements.txt
```

The core assessment works perfectly without pandas - it's only needed for optional analytics!

---

## 📁 File Structure

```
├── questions/
│   ├── basic_python.py          # Questions 1-5 (20 points)
│   ├── intermediate_python.py   # Questions 6-10 (25 points)
│   ├── advanced_python.py       # Questions 11-15 (30 points)
│   └── backend_development.py   # Questions 16-20 (25 points)
├── tests/                       # Test files (DO NOT MODIFY)
├── time_tracker.py              # Optional time tracking tool
├── requirements.txt             # Dependencies
├── requirements_python313.txt   # Python 3.13 compatible
└── README.md                    # Overview
```

---

## ⏱️ Time Tracking (Optional)

**Track your progress and learn about your coding patterns!**

### Quick Commands
```bash
# Start timing a category
python time_tracker.py start_basic        # Basic Python (Q1-Q5)
python time_tracker.py start_intermediate # Intermediate (Q6-Q10)  
python time_tracker.py start_advanced     # Advanced (Q11-Q15)
python time_tracker.py start_backend      # Backend (Q16-Q20)
python time_tracker.py start_setup        # Setup/debugging time

# End current session
python time_tracker.py end

# Log a submission (before git push)
python time_tracker.py submit

# View your time summary
python time_tracker.py summary
```

### Why Use Time Tracking?

✅ **Learn about your coding habits**  
✅ **Identify which topics take more time**  
✅ **Track improvement over multiple assignments**  
✅ **Get efficiency feedback**  
✅ **Completely optional and private**

### Example Workflow
```bash
# Start working on basic questions
python time_tracker.py start_basic

# Work on questions 1-5...

# End session when taking a break
python time_tracker.py end

# Later, start working on intermediate questions
python time_tracker.py start_intermediate

# Before pushing your code
python time_tracker.py submit
git add .
git commit -m "Completed Q1-Q7"
git push
```

---

## 📝 Question Overview

### Basic Python (20 points)
- **Q1**: Sum of numbers in a list
- **Q2**: Find largest number in a list
- **Q3**: Reverse a string without built-in methods
- **Q4**: Count vowels in a string (case-insensitive)
- **Q5**: Calculate nth Fibonacci number

### Intermediate Python (25 points)
- **Q6**: Create a BankAccount class with deposit/withdraw
- **Q7**: Safe division with error handling
- **Q8**: Word frequency counter from text
- **Q9**: JSON file read/write operations
- **Q10**: Advanced list processing (remove duplicates, filter, sort)

### Advanced Python (30 points)
- **Q11**: Create a timing decorator
- **Q12**: Fibonacci generator (memory efficient)
- **Q13**: File context manager with proper cleanup
- **Q14**: Thread-safe counter class
- **Q15**: Advanced data processing (filter, group, aggregate) - **Pure Python**

### Backend Development (25 points)
- **Q16**: Create REST API with Flask (CRUD operations)
- **Q17**: Database operations with SQLite
- **Q18**: Authentication system (password hashing + JWT)
- **Q19**: API testing suite
- **Q20**: Deployment configuration management

---

## 🛠️ Implementation Tips

### General Guidelines
- Read function docstrings carefully for requirements
- Pay attention to edge cases mentioned in examples
- Use meaningful variable names
- Add comments for complex logic
- Handle errors gracefully

### Testing Your Code
```bash
# Test all questions
pytest tests/

# Test specific category
pytest tests/test_basic_python.py
pytest tests/test_intermediate_python.py
pytest tests/test_advanced_python.py
pytest tests/test_backend_development.py

# Run with verbose output
pytest tests/ -v

# Run specific test
pytest tests/test_basic_python.py::TestQuestion1SumOfNumbers -v
```

### Common Patterns

#### Basic Python
```python
# List processing
def process_list(items):
    if not items:  # Handle empty list
        return 0
    # Your logic here
    return result

# String manipulation
def process_string(text):
    text = text.lower()  # Case insensitive
    # Your logic here
    return result
```

#### Object-Oriented Programming
```python
class MyClass:
    def __init__(self, param):
        self.param = param
    
    def method(self):
        # Your logic here
        return result
```

#### Error Handling
```python
def safe_function():
    try:
        # Risky operation
        return result
    except SpecificError:
        return None  # Or handle appropriately
```

#### File Operations
```python
def file_operation(filename, data):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
        with open(filename, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return None
```

---

## 🎯 Success Strategies

### Time Management
- Start with Basic Python questions (easier)
- Don't spend too much time on any single question
- Get partial credit rather than perfect solutions
- Save Backend Development for last (most complex)
- **Recommended time allocation:**
  - Basic Python: 45-60 minutes
  - Intermediate Python: 60-75 minutes
  - Advanced Python: 75-90 minutes
  - Backend Development: 60-75 minutes

### Code Quality
- Follow Python naming conventions (snake_case)
- Use docstrings and comments
- Keep functions focused and small
- Handle edge cases (empty inputs, None values)

### Debugging
- Use print statements to debug
- Test with simple inputs first
- Check return types match expectations
- Read error messages carefully

### Common Mistakes to Avoid
- Not handling empty lists/strings
- Forgetting to return values
- Case sensitivity issues
- Not implementing required methods in classes
- Modifying function signatures

---

## 📊 Grading Information

### Point Distribution
- **Basic Python**: 20 points (3, 3, 4, 5, 5)
- **Intermediate Python**: 25 points (5 each)
- **Advanced Python**: 30 points (6 each)
- **Backend Development**: 25 points (5 each)

### Grading Scale
- **90-100**: Excellent (A)
- **80-89**: Good (B)
- **70-79**: Satisfactory (C)
- **60-69**: Needs Improvement (D)
- **Below 60**: Unsatisfactory (F)

### What Graders Look For
1. **Correctness**: Does the code work as specified?
2. **Edge Cases**: Are unusual inputs handled?
3. **Code Quality**: Is the code readable and well-structured?
4. **Error Handling**: Are exceptions managed appropriately?

---

## 🕒 Time Expectations

### Realistic Time Estimates
- **Total assessment**: 3-4 hours for most students
- **Quick completion**: 2-2.5 hours (experienced programmers)
- **Extended time**: 4-6 hours (learning as you go)

### If You're Struggling
- **After 1 hour on one question**: Move on, come back later
- **After 4 hours total**: Consider which questions to prioritize
- **After 6 hours**: Focus on completing easier questions for partial credit

### Work Schedule Tips
- **Take breaks**: 15-minute break every hour
- **Multiple sessions**: Don't try to finish in one sitting
- **Peak hours**: Work when you're mentally fresh
- **Avoid all-nighters**: Code quality suffers when tired

---

## 🆘 Getting Help

### Before Asking for Help
1. Read the question docstring completely
2. Look at the provided examples
3. Run the tests to see what's failing
4. Check your function signature matches exactly

### Debugging Checklist
- [ ] Function name spelled correctly?
- [ ] All required parameters included?
- [ ] Correct return type?
- [ ] Edge cases handled?
- [ ] No syntax errors?

### Common Installation Issues

#### "pandas installation failed"
```bash
# Use core requirements (pandas removed for compatibility)
pip install -r requirements.txt
```

#### "bcrypt installation failed"
```bash
# Install build tools first
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

#### "pytest not found"
```bash
# Ensure you're in correct directory and virtual environment
which python
pip install pytest
```

### Resources
- Python documentation: https://docs.python.org/3/
- Flask documentation: https://flask.palletsprojects.com/
- pytest documentation: https://docs.pytest.org/

---

## 🏆 Final Tips

1. **Start Early**: Don't wait until the last minute
2. **Test Frequently**: Run tests after each function
3. **Read Carefully**: Understanding requirements is crucial
4. **Stay Calm**: If stuck, move to the next question
5. **Check GitHub**: Ensure your final code is pushed
6. **Use Time Tracking**: Learn about your coding patterns (optional)
7. **Focus on Learning**: This is about skill development, not just grades

### Your Success Metrics
- **Completion**: Did you attempt all questions?
- **Understanding**: Can you explain your solutions?
- **Efficiency**: Did you manage your time well?
- **Quality**: Is your code clean and readable?
- **Growth**: What did you learn from this assessment?

Good luck! 🍀 