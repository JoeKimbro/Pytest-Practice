"""
Your pytest practice playground.

Run all tests from this folder with:    pytest
Run with more detail:                   pytest -v
Run just one test file:                 pytest test_functions.py
Run one specific test:                  pytest test_functions.py::test_add_positive_numbers
Stop at the first failure:              pytest -x

A test is just a function whose name starts with `test_`. Inside it you make
some calls and use `assert` to state what you expect. If the assert is False,
the test fails.

Below are a FEW worked examples covering the main pytest features. After that
there's a big TODO list of functions waiting for you to test yourself.
"""

import pytest

import functions_to_test as f


# ===========================================================================
# WORKED EXAMPLES — study these, then write your own below
# ===========================================================================

# --- The most basic test: call a function, assert the result ---------------
def test_add_positive_numbers():
    assert f.add(2, 3) == 5


def test_add_negative_numbers():
    assert f.add(-1, -1) == -2


# --- Testing a True/False function -----------------------------------------
def test_is_even_with_even_number():
    assert f.is_even(4) is True


def test_is_even_with_odd_number():
    assert f.is_even(7) is False


# --- pytest.approx: for floats, never use == directly ----------------------
def test_to_celsius_freezing_point():
    # 32F is 0C. Floating point math is imprecise, so use approx.
    assert f.to_celsius(32) == pytest.approx(0)


def test_to_celsius_boiling_point():
    assert f.to_celsius(212) == pytest.approx(100)


# --- pytest.raises: asserting that a function raises an exception -----------
def test_grade_rejects_score_above_100():
    with pytest.raises(ValueError):
        f.grade(101)


def test_safe_divide_by_zero_message():
    # You can also inspect the exception message with `match`.
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        f.safe_divide(10, 0)


# --- @parametrize: run the same test with many inputs ----------------------
# This single test actually runs 4 times, once per (score, expected) pair.
@pytest.mark.parametrize("score, expected", [
    (95, "A"),
    (85, "B"),
    (72, "C"),
    (50, "F"),
])
def test_grade_letters(score, expected):
    assert f.grade(score) == expected


# --- Fixtures: reusable setup shared across tests --------------------------
# A fixture is a function decorated with @pytest.fixture. Any test that lists
# its name as an argument gets the returned value, freshly built each time.
@pytest.fixture
def account():
    return f.BankAccount(balance=100)


def test_account_starts_with_given_balance(account):
    assert account.balance == 100


def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw_too_much_raises(account):
    with pytest.raises(ValueError, match="insufficient funds"):
        account.withdraw(999)

def test_positiveAbsoluteVal(): 
    assert f.absolute_value(5) == 5

def test_negativeAbsoluteVal(): 
    assert f.absolute_value(-5) == 5

def test_zeroAbs(): 
    assert f.absolute_value(0) == 0

def test_reverseStringNormal():
    assert f.reverse_string("backwards") == "sdrawkcab"

def test_emptyReverse():
    assert f.reverse_string("") == ""

@pytest.mark.parametrize("value, low, high, expected", [
    (2,5,9, 5),
    (6,5,9,6),
    (1,4,7,4),
    (2,7,9,7),
])
def test_clamp(value, low, high, expected):
    assert f.clamp(value, low, high) == expected

@pytest.mark.parametrize("value, output", [
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (17, "17"),
])
def test_fizzbuzz(value, output):
    assert f.fizzbuzz(value) == output

def test_countVowels():
    assert f.count_vowels("Racecar") == 3 

def test_countVowelsWrong():
    assert not f.count_vowels("Racecar") == 4

def test_errorfactorial():
    with pytest.raises(ValueError):
        f.factorial(-1)

def test_1factorial():
    assert f.factorial(0) == 1

def test_Nfactorial():
    assert f.factorial(5) == 120


# ===========================================================================
# YOUR TURN — write tests for the functions below.
# Delete each TODO as you go. Aim to cover the normal case AND the edge cases
# hinted at in each function's docstring in functions_to_test.py.
# ===========================================================================

# TODO: absolute_value(n)      -- try positive, negative, and zero
# TODO: reverse_string(s)      -- try a normal string and an empty string ""
# TODO: clamp(value, low, high) -- value below, inside, and above the range
# TODO: fizzbuzz(n)            -- great candidate for @parametrize (3, 5, 15, 7)
# TODO: count_vowels(s)        -- mixed case, no vowels, empty string
# TODO: unique_sorted(items)   -- duplicates, already-sorted, empty list
# TODO: word_frequencies(text) -- repeated words, and notice the punctuation quirk
# TODO: flatten(nested)        -- normal, empty sublists, empty outer list
# TODO: second_largest(numbers) -- normal case, AND expect ValueError for [5] or [5, 5]
# TODO: factorial(n)           -- factorial(0) == 1, a normal value, and ValueError for -1
# TODO: is_palindrome(s)       -- "racecar", "A man a plan a canal Panama", "hello"
# TODO: fibonacci(n)           -- @parametrize the first several known values
# TODO: is_prime(n)            -- primes, non-primes, and edge cases 0, 1, 2
# TODO: BankAccount            -- use the `account` fixture; test transaction_count()
#                                 and that deposit(0) / withdraw(-5) raise ValueError


