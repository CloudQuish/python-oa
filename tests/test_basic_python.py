"""
Test cases for Basic Python Questions (1-5)
Each test is worth the points specified in the question docstring.
"""

import pytest
from questions.basic_python import (
    question_1_sum_of_numbers,
    question_2_find_largest,
    question_3_reverse_string,
    question_4_count_vowels,
    question_5_fibonacci
)


class TestQuestion1SumOfNumbers:
    """Test Question 1: Sum of Numbers (3 points)"""
    
    def test_sum_positive_numbers(self):
        """Test sum of positive numbers"""
        assert question_1_sum_of_numbers([1, 2, 3, 4, 5]) == 15
        assert question_1_sum_of_numbers([10, 20, 30]) == 60
    
    def test_sum_empty_list(self):
        """Test sum of empty list"""
        assert question_1_sum_of_numbers([]) == 0
    
    def test_sum_mixed_numbers(self):
        """Test sum of mixed positive and negative numbers"""
        assert question_1_sum_of_numbers([-1, 1, -2, 2]) == 0
        assert question_1_sum_of_numbers([-5, 10, -3, 8]) == 10
    
    def test_sum_floats(self):
        """Test sum of float numbers"""
        assert question_1_sum_of_numbers([1.5, 2.5, 3.0]) == 7.0


class TestQuestion2FindLargest:
    """Test Question 2: Find Largest Number (3 points)"""
    
    def test_find_largest_positive(self):
        """Test finding largest in positive numbers"""
        assert question_2_find_largest([1, 5, 3, 9, 2]) == 9
        assert question_2_find_largest([10, 20, 15, 25]) == 25
    
    def test_find_largest_empty(self):
        """Test finding largest in empty list"""
        assert question_2_find_largest([]) is None
    
    def test_find_largest_negative(self):
        """Test finding largest in negative numbers"""
        assert question_2_find_largest([-1, -5, -2]) == -1
        assert question_2_find_largest([-10, -3, -7]) == -3
    
    def test_find_largest_single(self):
        """Test finding largest in single element list"""
        assert question_2_find_largest([42]) == 42


class TestQuestion3ReverseString:
    """Test Question 3: Reverse String (4 points)"""
    
    def test_reverse_basic_string(self):
        """Test reversing basic strings"""
        assert question_3_reverse_string("hello") == "olleh"
        assert question_3_reverse_string("Python") == "nohtyP"
    
    def test_reverse_empty_string(self):
        """Test reversing empty string"""
        assert question_3_reverse_string("") == ""
    
    def test_reverse_single_char(self):
        """Test reversing single character"""
        assert question_3_reverse_string("a") == "a"
    
    def test_reverse_palindrome(self):
        """Test reversing palindrome"""
        assert question_3_reverse_string("racecar") == "racecar"
    
    def test_reverse_with_spaces(self):
        """Test reversing string with spaces"""
        assert question_3_reverse_string("hello world") == "dlrow olleh"


class TestQuestion4CountVowels:
    """Test Question 4: Count Vowels (5 points)"""
    
    def test_count_vowels_basic(self):
        """Test counting vowels in basic strings"""
        assert question_4_count_vowels("Hello World") == 3
        assert question_4_count_vowels("Python") == 1
    
    def test_count_vowels_case_insensitive(self):
        """Test case insensitive vowel counting"""
        assert question_4_count_vowels("PYTHON") == 1
        assert question_4_count_vowels("AEIOUaeiou") == 10
    
    def test_count_vowels_no_vowels(self):
        """Test counting vowels in strings with no vowels"""
        assert question_4_count_vowels("xyz") == 0
        assert question_4_count_vowels("bcdfg") == 0
    
    def test_count_vowels_empty_string(self):
        """Test counting vowels in empty string"""
        assert question_4_count_vowels("") == 0
    
    def test_count_vowels_all_vowels(self):
        """Test counting vowels in all vowel strings"""
        assert question_4_count_vowels("aeiou") == 5
        assert question_4_count_vowels("programming") == 3


class TestQuestion5Fibonacci:
    """Test Question 5: Fibonacci Sequence (5 points)"""
    
    def test_fibonacci_base_cases(self):
        """Test fibonacci base cases"""
        assert question_5_fibonacci(0) == 0
        assert question_5_fibonacci(1) == 1
    
    def test_fibonacci_small_numbers(self):
        """Test fibonacci for small numbers"""
        assert question_5_fibonacci(2) == 1
        assert question_5_fibonacci(3) == 2
        assert question_5_fibonacci(4) == 3
        assert question_5_fibonacci(5) == 5
    
    def test_fibonacci_larger_numbers(self):
        """Test fibonacci for larger numbers"""
        assert question_5_fibonacci(6) == 8
        assert question_5_fibonacci(7) == 13
        assert question_5_fibonacci(8) == 21
        assert question_5_fibonacci(10) == 55
    
    def test_fibonacci_sequence_property(self):
        """Test fibonacci sequence property: F(n) = F(n-1) + F(n-2)"""
        for n in range(2, 10):
            assert question_5_fibonacci(n) == question_5_fibonacci(n-1) + question_5_fibonacci(n-2) 