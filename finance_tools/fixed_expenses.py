import pandas as pd

class Fixed_Expenses:
    def __init__(self):
        self.fixed_expenses = []

    def get_fixed_expenses(self):
        return sum(Fixed_Expenses['Amount'])
    
    def add_fixed_expenses(self, expense, amount, note):
        self.fixed_expenses.append({
            'Expense': expense,
            'Amount': amount,
            'Note': note
        })
        
    def update_fixed_expenses(self, expense , amount, note):
        for expense in self.fixed_expenses:
               if expense['Expense'].lower() == expense.lower():
                    expense['Amount'] = amount
                    expense['Note'] = note
                    return f"Fixed Expenses updated for Expense: {expense}"
        return f"Fixed Expenses could not update for Expense: {expense}"
    
    def delete_fixed_expenses(self, expense):
            self.fixed_expenses = [i for i in self.fixed_expenses if i['Expense'].lower() != expense.lower()]
            return f"Fixed Expenses deleted for expense: {expense}"

my_fixed_expenses = Fixed_Expenses()

my_fixed_expenses.add_fixed_expenses('Mortgage', 3200, 'monthly')
my_fixed_expenses.delete_fixed_expenses('Utility')

