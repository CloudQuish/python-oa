"""
Test cases for Advanced Python Questions (11-15)
Each test is worth the points specified in the question docstring.
"""

import pytest
import time
import threading
import tempfile
import os
from io import StringIO
from contextlib import redirect_stdout
from questions.advanced_python import (
    question_11_timing_decorator,
    question_12_fibonacci_generator,
    question_13_file_manager,
    Question14ThreadSafeCounter,
    question_15_data_processor
)


class TestQuestion11TimingDecorator:
    """Test Question 11: Timing Decorator (6 points)"""
    
    def test_timing_decorator_functionality(self):
        """Test that decorator properly measures execution time"""
        @question_11_timing_decorator
        def test_function():
            time.sleep(0.1)
            return "done"
        
        # Capture stdout to check if timing is printed
        f = StringIO()
        with redirect_stdout(f):
            result = test_function()
        
        output = f.getvalue()
        assert result == "done"
        assert "test_function" in output
        assert "took" in output
        assert "seconds" in output
    
    def test_timing_decorator_with_parameters(self):
        """Test decorator with function that has parameters"""
        @question_11_timing_decorator
        def add_numbers(a, b):
            return a + b
        
        f = StringIO()
        with redirect_stdout(f):
            result = add_numbers(5, 3)
        
        assert result == 8
        output = f.getvalue()
        assert "add_numbers" in output
    
    def test_timing_decorator_preserves_function_name(self):
        """Test that decorator preserves function metadata"""
        @question_11_timing_decorator
        def original_function():
            """Original docstring"""
            return "original"
        
        # The decorator should preserve the original function name
        assert hasattr(original_function, '__name__')


class TestQuestion12FibonacciGenerator:
    """Test Question 12: Fibonacci Generator (6 points)"""
    
    def test_fibonacci_generator_basic(self):
        """Test basic fibonacci generator functionality"""
        result = list(question_12_fibonacci_generator(5))
        expected = [0, 1, 1, 2, 3]
        assert result == expected
    
    def test_fibonacci_generator_longer_sequence(self):
        """Test fibonacci generator with longer sequence"""
        result = list(question_12_fibonacci_generator(8))
        expected = [0, 1, 1, 2, 3, 5, 8, 13]
        assert result == expected
    
    def test_fibonacci_generator_zero(self):
        """Test fibonacci generator with zero"""
        result = list(question_12_fibonacci_generator(0))
        expected = []
        assert result == expected
    
    def test_fibonacci_generator_one(self):
        """Test fibonacci generator with one element"""
        result = list(question_12_fibonacci_generator(1))
        expected = [0]
        assert result == expected
    
    def test_fibonacci_generator_is_generator(self):
        """Test that function returns a generator"""
        fib_gen = question_12_fibonacci_generator(5)
        assert hasattr(fib_gen, '__next__')
        assert hasattr(fib_gen, '__iter__')


class TestQuestion13FileManager:
    """Test Question 13: Context Manager (6 points)"""
    
    def test_file_manager_basic_functionality(self):
        """Test basic file manager functionality"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            filename = temp_file.name
        
        try:
            # Test writing to file
            f = StringIO()
            with redirect_stdout(f):
                with question_13_file_manager(filename, "w") as file_obj:
                    file_obj.write("Hello World")
            
            output = f.getvalue()
            assert f"File opened: {filename}" in output
            assert f"File closed: {filename}" in output
            
            # Verify content was written
            with open(filename, 'r') as f:
                content = f.read()
                assert content == "Hello World"
                
        finally:
            if os.path.exists(filename):
                os.unlink(filename)
    
    def test_file_manager_read_mode(self):
        """Test file manager in read mode"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write("Test content")
            filename = temp_file.name
        
        try:
            f = StringIO()
            with redirect_stdout(f):
                with question_13_file_manager(filename, "r") as file_obj:
                    content = file_obj.read()
            
            assert content == "Test content"
            output = f.getvalue()
            assert f"File opened: {filename}" in output
            assert f"File closed: {filename}" in output
            
        finally:
            if os.path.exists(filename):
                os.unlink(filename)
    
    def test_file_manager_exception_handling(self):
        """Test file manager handles exceptions properly"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            filename = temp_file.name
        
        try:
            f = StringIO()
            with redirect_stdout(f):
                try:
                    with question_13_file_manager(filename, "w") as file_obj:
                        file_obj.write("Hello")
                        raise ValueError("Test exception")
                except ValueError:
                    pass  # Expected exception
            
            output = f.getvalue()
            assert f"File opened: {filename}" in output
            assert f"File closed: {filename}" in output
            
        finally:
            if os.path.exists(filename):
                os.unlink(filename)


class TestQuestion14ThreadSafeCounter:
    """Test Question 14: Thread-Safe Counter (6 points)"""
    
    def test_thread_safe_counter_basic_operations(self):
        """Test basic counter operations"""
        counter = Question14ThreadSafeCounter()
        assert counter.get_value() == 0
        
        counter.increment()
        assert counter.get_value() == 1
        
        counter.increment()
        assert counter.get_value() == 2
        
        counter.decrement()
        assert counter.get_value() == 1
        
        counter.reset()
        assert counter.get_value() == 0
    
    def test_thread_safe_counter_multiple_operations(self):
        """Test multiple operations on counter"""
        counter = Question14ThreadSafeCounter()
        
        for _ in range(10):
            counter.increment()
        assert counter.get_value() == 10
        
        for _ in range(5):
            counter.decrement()
        assert counter.get_value() == 5
    
    def test_thread_safe_counter_thread_safety(self):
        """Test thread safety with multiple threads"""
        counter = Question14ThreadSafeCounter()
        
        def increment_worker():
            for _ in range(100):
                counter.increment()
        
        def decrement_worker():
            for _ in range(50):
                counter.decrement()
        
        threads = []
        # Create multiple threads
        for _ in range(5):
            t1 = threading.Thread(target=increment_worker)
            t2 = threading.Thread(target=decrement_worker)
            threads.extend([t1, t2])
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Should have (5 * 100) - (5 * 50) = 250
        assert counter.get_value() == 250


class TestQuestion15DataProcessor:
    """Test Question 15: Advanced Data Processing (6 points)"""
    
    def test_data_processor_basic(self):
        """Test basic data processing"""
        data = [
            {"name": "Alice", "age": 25, "city": "NYC"},
            {"name": "Bob", "age": 17, "city": "NYC"},
            {"name": "Charlie", "age": 30, "city": "LA"},
            {"name": "Diana", "age": 22, "city": "NYC"}
        ]
        
        result = question_15_data_processor(data)
        expected = {'LA': 30.0, 'NYC': 23.5}
        assert result == expected
    
    def test_data_processor_filter_age(self):
        """Test age filtering (18+)"""
        data = [
            {"name": "Alice", "age": 25, "city": "NYC"},
            {"name": "Bob", "age": 16, "city": "NYC"},
            {"name": "Charlie", "age": 17, "city": "LA"},
            {"name": "Diana", "age": 18, "city": "LA"}
        ]
        
        result = question_15_data_processor(data)
        expected = {'NYC': 25.0, 'LA': 18.0}
        assert result == expected
    
    def test_data_processor_empty_list(self):
        """Test data processing with empty list"""
        result = question_15_data_processor([])
        assert result == {}
    
    def test_data_processor_single_city(self):
        """Test data processing with single city"""
        data = [
            {"name": "Alice", "age": 25, "city": "NYC"},
            {"name": "Bob", "age": 30, "city": "NYC"},
            {"name": "Charlie", "age": 35, "city": "NYC"}
        ]
        
        result = question_15_data_processor(data)
        expected = {'NYC': 30.0}
        assert result == expected
    
    def test_data_processor_sorting(self):
        """Test that results are sorted by average age (descending)"""
        data = [
            {"name": "Alice", "age": 20, "city": "NYC"},
            {"name": "Bob", "age": 40, "city": "LA"},
            {"name": "Charlie", "age": 30, "city": "Chicago"},
            {"name": "Diana", "age": 25, "city": "NYC"}
        ]
        
        result = question_15_data_processor(data)
        expected = {'LA': 40.0, 'Chicago': 30.0, 'NYC': 22.5}
        
        # Convert to list to check ordering
        result_items = list(result.items())
        expected_items = list(expected.items())
        
        assert result_items == expected_items 