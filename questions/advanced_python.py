"""
Advanced Python Questions (11-15) - 30 points total
These questions test advanced Python concepts including decorators,
generators, context managers, concurrency, and advanced data manipulation.
"""

import time
import threading
from functools import wraps
from contextlib import contextmanager
from typing import Generator, List, Dict, Any


def question_11_timing_decorator(func):
    """
    Question 11: Timing Decorator (6 points)
    
    Create a decorator that measures and prints the execution time of a function.
    The decorator should print: "Function {func_name} took {time:.4f} seconds"
    
    Args:
        func: Function to be decorated
        
    Returns:
        function: Decorated function
        
    Example:
        @question_11_timing_decorator
        def slow_function():
            time.sleep(0.1)
            return "done"
        
        # When called, should print timing information
    """
    # TODO: Implement the timing decorator
    pass


def question_12_fibonacci_generator(n):
    """
    Question 12: Fibonacci Generator (6 points)
    
    Create a generator that yields the first n Fibonacci numbers.
    This should be memory efficient and not store all numbers at once.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Yields:
        int: Next Fibonacci number
        
    Examples:
        >>> list(question_12_fibonacci_generator(5))
        [0, 1, 1, 2, 3]
        >>> list(question_12_fibonacci_generator(8))
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    # TODO: Implement the Fibonacci generator
    pass


@contextmanager
def question_13_file_manager(filename, mode='r'):
    """
    Question 13: Context Manager (6 points)
    
    Create a context manager that safely handles file operations.
    It should:
    - Open the file with the specified mode
    - Yield the file object
    - Automatically close the file, even if an exception occurs
    - Print "File opened: {filename}" when entering
    - Print "File closed: {filename}" when exiting
    
    Args:
        filename (str): Name of the file to open
        mode (str): File mode (default 'r')
        
    Yields:
        file: File object
        
    Example:
        with question_13_file_manager("test.txt", "w") as f:
            f.write("Hello World")
        # Should print open/close messages
    """
    # TODO: Implement the context manager
    pass


class Question14ThreadSafeCounter:
    """
    Question 14: Thread-Safe Counter (6 points)
    
    Create a thread-safe counter class that can be safely used across multiple threads.
    It should have:
    - __init__() method to initialize counter to 0
    - increment() method to add 1 to counter
    - decrement() method to subtract 1 from counter  
    - get_value() method to return current counter value
    - reset() method to set counter back to 0
    
    Use threading.Lock to ensure thread safety.
    
    Example:
        >>> counter = Question14ThreadSafeCounter()
        >>> counter.increment()
        >>> counter.get_value()
        1
        >>> counter.decrement()
        >>> counter.get_value()
        0
    """
    
    def __init__(self):
        # TODO: Initialize counter and lock
        pass
    
    def increment(self):
        # TODO: Thread-safe increment
        pass
    
    def decrement(self):
        # TODO: Thread-safe decrement
        pass
    
    def get_value(self):
        # TODO: Thread-safe get value
        pass
    
    def reset(self):
        # TODO: Thread-safe reset
        pass


def question_15_data_processor(data_list):
    """
    Question 15: Advanced Data Processing (6 points)
    
    Process a list of dictionaries representing people with the following operations:
    1. Filter people who are 18 years or older
    2. Group them by city
    3. Calculate average age for each city
    4. Return a dictionary with city as key and average age as value
    5. Sort the result by average age (descending)
    
    Args:
        data_list (list): List of dictionaries with 'name', 'age', 'city' keys
        
    Returns:
        dict: Dictionary with city as key and average age as value, sorted by age desc
        
    Example:
        >>> data = [
        ...     {"name": "Alice", "age": 25, "city": "NYC"},
        ...     {"name": "Bob", "age": 17, "city": "NYC"},
        ...     {"name": "Charlie", "age": 30, "city": "LA"},
        ...     {"name": "Diana", "age": 22, "city": "NYC"}
        ... ]
        >>> question_15_data_processor(data)
        {'LA': 30.0, 'NYC': 23.5}
    """
    # TODO: Implement advanced data processing
    pass 