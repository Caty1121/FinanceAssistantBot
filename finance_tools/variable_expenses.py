import pandas as pd

class Variable_Expenses:
    def __init__(self):
        self.variable_expenses = []

    def get_variable_expenses(self):
        return sum(Variable_Expenses['Amount'])
    
    def add_variable_expenses(self, expense, amount, note):
        self.variable_expenses.append({
            'Expense': expense,
            'Amount': amount,
            'Note': note
        })
        
    def update_variable_expenses(self, expense , amount, note):
        for expense in self.variable_expenses:
               if expense['Expense'].lower() == expense.lower():
                    expense['Amount'] = amount
                    expense['Note'] = note
                    return f"Variabele Expenses updated for Expense: {expense}"
        return f"Variable Expenses could not update for Expense: {expense}"
    
    def delete_variable_expenses(self, expense):
            self.variable_expenses = [i for i in self.variable_expenses if i['Expense'].lower() != expense.lower()]
            return f"Variable Expenses deleted for expense: {expense}"

my_variable_expenses = Variable_Expenses()

my_variable_expenses.add_variable_expenses('Netflix', 12.50, 'subscription')
my_variable_expenses.delete_variable_expenses('Emergency Fund')

