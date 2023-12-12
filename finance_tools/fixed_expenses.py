class FixedExpenses:
    def __init__(self, expenses=None):
        self.expenses = expenses if expenses is not None else {}

    def add_expense(self, name, amount):
        self.expenses[name] = amount

    def total_expenses(self):
        return sum(self.expenses.values())