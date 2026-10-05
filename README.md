# CLI Expense Tracker

A simple command-line expense tracker built in Python, demonstrating OOP design, file persistence, exception handling, and automated testing.

## Features
- Add expenses with description, amount, and category
- Input validation (rejects non-positive amounts)
- Totals across all recorded expenses
- Saves and loads expenses from a local file, so data persists between runs

## Concepts demonstrated
- Object-oriented design (composition: `ExpenseTracker` manages a list of `Expense` objects)
- File I/O (`open`, reading/writing structured text)
- Exception handling (`try`/`except`, custom validation with `raise ValueError`)
- Type hints
- Unit testing with `pytest`

## Installation
```bash
git clone <your-repo-url>
cd expense-tracker
pip install -r requirements.txt
```

## Usage
```bash
python expense_tracker.py
```

## Running tests
```bash
pytest
```

## Possible future improvements
- Use Python's `csv` module instead of manual comma-splitting, to safely handle descriptions containing commas
- Add a proper CLI interface (e.g. with `argparse`) instead of hardcoded sample data