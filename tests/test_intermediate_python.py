"""
Test cases for Intermediate Python Questions (6-10)
Each test is worth the points specified in the question docstring.
"""

import pytest
import json
import os
import tempfile
from questions.intermediate_python import (
    Question6BankAccount,
    question_7_safe_divide,
    question_8_word_frequency,
    question_9_file_operations,
    question_10_list_manipulation
)


class TestQuestion6BankAccount:
    """Test Question 6: Bank Account Class (5 points)"""
    
    def test_bank_account_initialization(self):
        """Test bank account initialization"""
        account = Question6BankAccount("12345", 100)
        assert account.get_balance() == 100
        
        account_default = Question6BankAccount("67890")
        assert account_default.get_balance() == 0
    
    def test_deposit(self):
        """Test deposit functionality"""
        account = Question6BankAccount("12345", 100)
        account.deposit(50)
        assert account.get_balance() == 150
        
        account.deposit(25.50)
        assert account.get_balance() == 175.50
    
    def test_withdraw_sufficient_funds(self):
        """Test withdrawal with sufficient funds"""
        account = Question6BankAccount("12345", 100)
        result = account.withdraw(30)
        assert result is True
        assert account.get_balance() == 70
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds"""
        account = Question6BankAccount("12345", 100)
        result = account.withdraw(150)
        assert result is False
        assert account.get_balance() == 100
    
    def test_withdraw_exact_balance(self):
        """Test withdrawal of exact balance"""
        account = Question6BankAccount("12345", 100)
        result = account.withdraw(100)
        assert result is True
        assert account.get_balance() == 0


class TestQuestion7SafeDivide:
    """Test Question 7: Safe Division with Error Handling (5 points)"""
    
    def test_safe_divide_normal(self):
        """Test normal division"""
        assert question_7_safe_divide(10, 2) == 5.0
        assert question_7_safe_divide(15, 3) == 5.0
        assert question_7_safe_divide(7, 2) == 3.5
    
    def test_safe_divide_by_zero(self):
        """Test division by zero"""
        assert question_7_safe_divide(10, 0) is None
        assert question_7_safe_divide(0, 0) is None
    
    def test_safe_divide_type_error(self):
        """Test division with invalid types"""
        assert question_7_safe_divide("10", 2) is None
        assert question_7_safe_divide(10, "2") is None
        assert question_7_safe_divide("10", "2") is None
    
    def test_safe_divide_negative_numbers(self):
        """Test division with negative numbers"""
        assert question_7_safe_divide(-10, 2) == -5.0
        assert question_7_safe_divide(10, -2) == -5.0
        assert question_7_safe_divide(-10, -2) == 5.0


class TestQuestion8WordFrequency:
    """Test Question 8: Word Frequency Counter (5 points)"""
    
    def test_word_frequency_basic(self):
        """Test basic word frequency counting"""
        result = question_8_word_frequency("Hello world hello")
        expected = {'hello': 2, 'world': 1}
        assert result == expected
    
    def test_word_frequency_with_punctuation(self):
        """Test word frequency with punctuation"""
        result = question_8_word_frequency("Python is great! Python rocks.")
        expected = {'python': 2, 'is': 1, 'great': 1, 'rocks': 1}
        assert result == expected
    
    def test_word_frequency_empty_string(self):
        """Test word frequency with empty string"""
        result = question_8_word_frequency("")
        assert result == {}
    
    def test_word_frequency_case_insensitive(self):
        """Test case insensitive word frequency"""
        result = question_8_word_frequency("The THE the")
        expected = {'the': 3}
        assert result == expected
    
    def test_word_frequency_single_word(self):
        """Test word frequency with single word"""
        result = question_8_word_frequency("programming")
        expected = {'programming': 1}
        assert result == expected


class TestQuestion9FileOperations:
    """Test Question 9: JSON File Operations (5 points)"""
    
    def test_file_operations_basic(self):
        """Test basic file operations"""
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            filename = f.name
        
        try:
            result = question_9_file_operations(filename, data)
            assert result == data
        finally:
            if os.path.exists(filename):
                os.unlink(filename)
    
    def test_file_operations_complex_data(self):
        """Test file operations with complex data"""
        data = {
            "users": [
                {"name": "Alice", "age": 25, "active": True},
                {"name": "Bob", "age": 30, "active": False}
            ],
            "metadata": {"version": "1.0", "created": "2023-01-01"}
        }
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            filename = f.name
        
        try:
            result = question_9_file_operations(filename, data)
            assert result == data
        finally:
            if os.path.exists(filename):
                os.unlink(filename)
    
    def test_file_operations_error_handling(self):
        """Test file operations error handling"""
        data = {"name": "John", "age": 30}
        # Use invalid filename that should cause an error
        result = question_9_file_operations("/invalid/path/file.json", data)
        assert result is None


class TestQuestion10ListManipulation:
    """Test Question 10: Advanced List Manipulation (5 points)"""
    
    def test_list_manipulation_basic(self):
        """Test basic list manipulation"""
        result = question_10_list_manipulation([4, 2, 7, 2, 8, 4, 1, 9, 8])
        expected = [2, 4, 8]
        assert result == expected
    
    def test_list_manipulation_no_even_numbers(self):
        """Test list manipulation with no even numbers"""
        result = question_10_list_manipulation([1, 3, 5, 7])
        expected = []
        assert result == expected
    
    def test_list_manipulation_duplicates(self):
        """Test list manipulation with duplicates"""
        result = question_10_list_manipulation([10, 20, 10, 30, 20])
        expected = [10, 20, 30]
        assert result == expected
    
    def test_list_manipulation_all_even(self):
        """Test list manipulation with all even numbers"""
        result = question_10_list_manipulation([2, 4, 6, 8, 2, 4])
        expected = [2, 4, 6, 8]
        assert result == expected
    
    def test_list_manipulation_empty_list(self):
        """Test list manipulation with empty list"""
        result = question_10_list_manipulation([])
        expected = []
        assert result == expected
    
    def test_list_manipulation_order_preservation(self):
        """Test that order is preserved before sorting"""
        result = question_10_list_manipulation([8, 2, 4, 6, 2, 8])
        expected = [2, 4, 6, 8]
        assert result == expected 