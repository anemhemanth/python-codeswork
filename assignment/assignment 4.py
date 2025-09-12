# my_programs.py
# 15 different Python programs stored as functions

def armstrong_number():
    print("Program: Armstrong Number\n")
    print(""" 
def is_armstrong(num):
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    return num == total
    """)
    print("Test Case 1: is_armstrong(153) -> True")
    print("Test Case 2: is_armstrong(123) -> False")
    print("Explanation: An Armstrong number is equal to the sum of its own digits each raised to the power of the number of digits.\n")


def swap_numbers():
    print("Program: Swap Two Numbers\n")
    print("""
def swap(a, b):
    a, b = b, a
    return a, b
    """)
    print("Test Case 1: swap(10, 20) -> (20, 10)")
    print("Test Case 2: swap(5, -1) -> (-1, 5)")
    print("Explanation: This uses Python’s tuple unpacking feature to swap two values without a temporary variable.\n")


def gcd_numbers():
    print("Program: GCD of Two Numbers\n")
    print("""
import math
def gcd(a, b):
    return math.gcd(a, b)
    """)
    print("Test Case 1: gcd(12, 18) -> 6")
    print("Test Case 2: gcd(7, 13) -> 1")
    print("Explanation: Uses Euclid’s algorithm via math.gcd to compute the greatest common divisor.\n")


def reverse_number():
    print("Program: Reverse a Number\n")
    print("""
def reverse_num(n):
    return int(str(n)[::-1])
    """)
    print("Test Case 1: reverse_num(123) -> 321")
    print("Test Case 2: reverse_num(1005) -> 5001")
    print("Explanation: Converts number to string, reverses it, and converts back to integer.\n")


def sum_of_digits():
    print("Program: Sum of Digits\n")
    print("""
def sum_digits(n):
    return sum(int(d) for d in str(n))
    """)
    print("Test Case 1: sum_digits(123) -> 6")
    print("Test Case 2: sum_digits(987) -> 24")
    print("Explanation: Iterates over digits of the number and sums them.\n")


def count_vowels():
    print("Program: Count Vowels in a String\n")
    print("""
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
    """)
    print("Test Case 1: count_vowels('hello') -> 2")
    print("Test Case 2: count_vowels('Python') -> 1")
    print("Explanation: Counts characters that belong to vowel set.\n")


def palindrome_check():
    print("Program: Palindrome Check\n")
    print("""
def is_palindrome(s):
    return s == s[::-1]
    """)
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome('hello') -> False")
    print("Explanation: A palindrome reads the same forward and backward.\n")


def factorial_number():
    print("Program: Factorial of a Number\n")
    print("""
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
    """)
    print("Test Case 1: factorial(5) -> 120")
    print("Test Case 2: factorial(0) -> 1")
    print("Explanation: Uses recursion to compute factorial.\n")


def fibonacci_series():
    print("Program: Fibonacci Series\n")
    print("""
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
    """)
    print("Test Case 1: fibonacci(5) -> [0, 1, 1, 2, 3]")
    print("Test Case 2: fibonacci(7) -> [0, 1, 1, 2, 3, 5, 8]")
    print("Explanation: Builds sequence by summing previous two numbers.\n")


def prime_check():
    print("Program: Prime Number Check\n")
    print("""
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
    """)
    print("Test Case 1: is_prime(7) -> True")
    print("Test Case 2: is_prime(10) -> False")
    print("Explanation: Checks divisibility up to square root of n.\n")


def count_words():
    print("Program: Count Words in a Sentence\n")
    print("""
def count_words(s):
    return len(s.split())
    """)
    print("Test Case 1: count_words('Hello world') -> 2")
    print("Test Case 2: count_words('Python is great') -> 3")
    print("Explanation: Splits string by spaces and counts parts.\n")


def decimal_to_binary():
    print("Program: Convert Decimal to Binary\n")
    print("""
def dec_to_bin(n):
    return bin(n).replace('0b','')
    """)
    print("Test Case 1: dec_to_bin(10) -> '1010'")
    print("Test Case 2: dec_to_bin(7) -> '111'")
    print("Explanation: Uses Python’s built-in bin function.\n")


def string_title_case():
    print("Program: Convert String to Title Case\n")
    print("""
def to_title(s):
    return s.title()
    """)
    print("Test Case 1: to_title('hello world') -> 'Hello World'")
    print("Test Case 2: to_title('python programming') -> 'Python Programming'")
    print("Explanation: Uses str.title() method to capitalize words.\n")


def largest_number_list():
    print("Program: Find Largest Number in List\n")
    print("""
def largest(lst):
    return max(lst)
    """)
    print("Test Case 1: largest([1, 5, 3]) -> 5")
    print("Test Case 2: largest([-1, -9, 0]) -> 0")
    print("Explanation: Uses built-in max() function to find the largest element.\n")


def custom_sort():
    print("Program: Custom Sort (Descending)\n")
    print("""
def custom_sort(lst):
    return sorted(lst, reverse=True)
    """)
    print("Test Case 1: custom_sort([3,1,4,2]) -> [4,3,2,1]")
    print("Test Case 2: custom_sort([10,5,8]) -> [10,8,5]")
    print("Explanation: Uses sorted() with reverse=True for descending order.\n")
