import pytest
from expense_tracker import ExpenseTracker


def test_add_expense_increase_count():
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 5, "Food")
    assert len(tracker.expenses) == 1


def test_negative_amount_raises_error():
    tracker = ExpenseTracker()
    with pytest.raises(ValueError):
        tracker.add_expense("Refund", -5, "Misc")


def test_total_calculates_correctly():
    tracker = ExpenseTracker()
    tracker.add_expense("Mocha", 10.0, "Food")
    tracker.add_expense("Flight ticket", 5.0, "Transport")
    tracker.add_expense("Concert", 10.0, "Entertainment")
    assert tracker.total() == 25.0