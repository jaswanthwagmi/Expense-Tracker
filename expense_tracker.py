from typing import Optional


class Expense:
    def __init__(self, description: str, amount: float, category: str):
        self.description = description
        self.amount = amount
        self.category = category


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description: str, amount: float, category: str) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        new_expense = Expense(description, amount, category)
        self.expenses.append(new_expense)

    def total(self) -> float:
        total_amount = 0
        for expense in self.expenses:
            total_amount += expense.amount
        return total_amount

    def list_expenses(self) -> None:
        for expense in self.expenses:
            print(f"{expense.description}: ${expense.amount} ({expense.category})")

    def save_to_file(self, filename: str) -> None:
        with open(filename, "w") as file:
            for expense in self.expenses:
                file.write(f"{expense.description},{expense.amount},{expense.category}\n")

    def load_from_file(self, filename: str) -> None:
        self.expenses = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    description, amount, category = line.strip().split(",")
                    amount = float(amount)
                    expense = Expense(description, amount, category)
                    self.expenses.append(expense)
        except FileNotFoundError:
            self.expenses = []


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.load_from_file("expenses.txt")

    tracker.add_expense("Coffee", 4.5, "Food")
    tracker.add_expense("Bus ticket", 2.0, "Transport")

    tracker.list_expenses()
    print(f"Total: {tracker.total()}")

    tracker.save_to_file("expenses.txt")