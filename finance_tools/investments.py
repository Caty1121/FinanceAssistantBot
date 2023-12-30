class Investment:
    def __init__(self):
        self.investments = []

    def add_investments(self, source, amount, note):
        self.investments.append({
            'Source' : source,
            'Amount': amount,
            'Note': note
         })

    def get_total_investments(self):
        return sum(investment['Amount'] for investment in self.investments)
    
    def get_investment_details(self, source):
        for investment in self.investments:
            if investment['Source'].lower() == source.lower():
                return investment
        return f"No investment found for source: {source}"
    
    def update_investment(self, source, amount, note):
        for investment in self.investments:
            if investment['Source'].lower() == source.lower():
                investment['Amount'] = amount
                investment['Note'] = note
                return f"Investment updated for source: {source}"
        return f"No investment found for source: {source}"
    
    def delete_investment(self, source):
        self.investments = [i for i in self.investments if i['Source'].lower() != source.lower()]
        return f"Investment deleted for source: {source}"

    
my_investments = Investment()

my_investments.add_investments('Emergency Fund', 200, 'Monthly Contribution')
my_investments.add_investments('College Fund', 200, 'Monthly Investment')
        

print(my_investments.get_total_investments())
print(my_investments.get_investment_details('Emergency Fund'))

## Update Example
# my_investments.update_investment('College Fund', 600, 'Updated Monthly Investment')

## Delete Example
# my_investments.delete_investment('Emergency Fund')