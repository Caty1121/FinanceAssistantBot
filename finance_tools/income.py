#import pandas as pd

class Income:
    def __init__(self):
        self.income_sources = []

    def add_income(self, source, amount, frequency):
        self.income_sources.append({'Source': source, 'Amount': amount, 'Frequency': frequency})

    def calculate_total_income(self):
        return sum(item['Amount'] for item in self.income_sources)