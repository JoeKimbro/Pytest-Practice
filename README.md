# Pytest Practice

A personal practice project for learning software testing with **pytest** and
Python. The goal is to build the core skill of a QA / test engineer: looking at
a piece of code and instinctively asking *"what inputs break this?"*

## What's in here

| File | Purpose |
|------|---------|
| `functions_to_test.py` | A collection of 18 functions plus a `BankAccount` class, organized from easy to hard. These are the "code under test." |
| `test_functions.py` | The test suite. Contains a few worked examples of pytest features, then my own tests written from scratch. |
| `README.md` | This file. |

## What I'm practicing

- Writing tests that cover the **normal case** *and* the **edge cases**
  (empty inputs, zero, negatives, duplicates, boundaries).
- Core pytest features:
  - Basic `assert` statements
  - `pytest.approx` for comparing floats
  - `pytest.raises` for testing that exceptions fire correctly
  - `@pytest.mark.parametrize` for running one test against many inputs
  - **Fixtures** for reusable setup (e.g. a fresh `BankAccount` per test)
- Reading and understanding **test failure output** to debug code.

## How to run the tests

From this folder:

```bash
# Run everything
python -m pytest

# Verbose — show each test name and result
python -m pytest -v

# Stop at the first failure
python -m pytest -x

# Run a single test file
python -m pytest test_functions.py

# Run one specific test
python -m pytest test_functions.py::test_add_positive_numbers
```

> Note: `python -m pytest` is used instead of the bare `pytest` command so it
> works regardless of whether pytest is on the system PATH.

## Progress

- [x] Set up project and worked through example tests
- [ ] Write tests for all functions in `functions_to_test.py`
- [ ] Measure coverage with `python -m pytest --cov`
- [ ] Practice debugging by hunting deliberately introduced bugs
