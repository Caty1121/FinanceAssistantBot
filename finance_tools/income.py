#import pandas as pd
class Income:
    def __init__(self):
        self.income_sources = []

    def get_total_income(self):
        return sum(income['Amount'] for income in self.income)

    def add_income(self, source, amount, frequency):
        self.income_sources.append({
            'Source': source,
            'Amount': amount,
            'Frequency': frequency
            })

    def calculate_total_income(self):
        return sum(item['Amount'] for item in self.income_sources)
    
    def update_income(self, source, amount, frequency):
        for income in self.income_sources:
            if income['Source'].lower() == source.lower():
                income['Amount'] = amount
                income['Frequency'] = frequency 
                return f"Income updated for {source}"
        return f"No income found for {source}"
    
    def delete_income(self, source):
        self.income = [i for i in self.income if i['Source'].lower() != source.lower()]
        return f"Income deleted for source: {source}"
    
my_income = Income()

my_income.add_income('Salary', 100000, 'Annually')
my_income.delete_income('401K Match', 10, 'Monthly')


    ## TODO ## finish crud, ref investments.py

print(my_income.get_total_income())
