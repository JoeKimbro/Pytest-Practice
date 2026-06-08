"""
Functions to practice testing with pytest.

These are organized roughly from easiest to hardest to test. Each one is a
self-contained, working function. Your job is to write tests for them in
test_functions.py.

Some functions intentionally raise exceptions, handle edge cases, or have
tricky behavior — those are good candidates for learning specific pytest
features (parametrize, raises, approx, fixtures, etc.).
"""


# ---------------------------------------------------------------------------
# LEVEL 1 — Simple, pure functions (good for your very first tests)
# ---------------------------------------------------------------------------

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def absolute_value(n):
    """Return the absolute value of a number (without using abs())."""
    if n < 0:
        return -n
    return n


def reverse_string(s):
    """Return the string reversed."""
    return s[::-1]


# ---------------------------------------------------------------------------
# LEVEL 2 — Conditionals and edge cases (think: what inputs break these?)
# ---------------------------------------------------------------------------

def grade(score):
    """
    Convert a numeric score (0-100) to a letter grade.

    Raises ValueError if the score is outside 0-100.
    """
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def safe_divide(a, b):
    """
    Divide a by b. Raises ZeroDivisionError with a friendly message
    if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def clamp(value, low, high):
    """
    Constrain value to the range [low, high].

    Returns low if value < low, high if value > high, otherwise value.
    """
    if value < low:
        return low
    if value > high:
        return high
    return value


def fizzbuzz(n):
    """
    Classic FizzBuzz for a single number.

    Returns "Fizz" if divisible by 3, "Buzz" if divisible by 5,
    "FizzBuzz" if divisible by both, otherwise the number as a string.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


# ---------------------------------------------------------------------------
# LEVEL 3 — Collections and strings (test with empty inputs, duplicates, etc.)
# ---------------------------------------------------------------------------

def count_vowels(s):
    """Count the number of vowels (a, e, i, o, u) in a string, case-insensitive."""
    return sum(1 for char in s.lower() if char in "aeiou")


def unique_sorted(items):
    """Return a sorted list of the unique items in the input iterable."""
    return sorted(set(items))


def word_frequencies(text):
    """
    Return a dict mapping each lowercase word to how many times it appears.
    Words are split on whitespace; punctuation is NOT stripped (a known quirk!).
    """
    freqs = {}
    for word in text.lower().split():
        freqs[word] = freqs.get(word, 0) + 1
    return freqs


def flatten(nested):
    """
    Flatten one level of nesting in a list of lists.

    e.g. [[1, 2], [3], [4, 5]] -> [1, 2, 3, 4, 5]
    """
    result = []
    for sublist in nested:
        for item in sublist:
            result.append(item)
    return result


def second_largest(numbers):
    """
    Return the second largest UNIQUE number in a list.

    Raises ValueError if there are fewer than two unique numbers.
    """
    unique = sorted(set(numbers), reverse=True)
    if len(unique) < 2:
        raise ValueError("need at least two unique numbers")
    return unique[1]


# ---------------------------------------------------------------------------
# LEVEL 4 — More logic (loops, accumulation, classic algorithms)
# ---------------------------------------------------------------------------

def factorial(n):
    """
    Return n! (n factorial).

    Raises ValueError for negative input. factorial(0) == 1.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_palindrome(s):
    """
    Return True if s reads the same forwards and backwards, ignoring case
    and spaces. (Punctuation IS considered — another quirk to test!)
    """
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def fibonacci(n):
    """
    Return the nth Fibonacci number (0-indexed).
    fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(2) == 1, ...

    Raises ValueError for negative input.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# ---------------------------------------------------------------------------
# LEVEL 5 — A small class (practice fixtures and testing stateful objects)
# ---------------------------------------------------------------------------

class BankAccount:
    """A minimal bank account. Good for practicing setup with fixtures."""

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("starting balance cannot be negative")
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
        return self.balance

    def transaction_count(self):
        return len(self.transactions)
