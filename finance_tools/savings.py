class Savings:
    def __init__(self):
            self.Savings = []

    def get_total_savings(self):
            return sum(Savings['Amount'] for Savings in self.Savings)
    
    def add_savings(self, goal, amount, note):
            self.Savings.append({
                   'Goal': goal,
                   'Amount': amount,
                   'Note': note
            })
        
    def update_savings(self, goal, amount, note):
        for save in self.Savings:
               if save['Goal'].lower() == goal.lower():
                    save['Amount'] = amount
                    save['Note'] = note
                    return f"Savings updated for goal: {goal}"
        return f"Savings could not update for goal: {goal}"
    
    def delete_savings(self, goal):
            self.Savings = [i for i in self.Savings if i['Goal'].lower() != goal.lower()]
            return f"Savings deleted for goal: {goal}"

my_savings = Savings()

my_savings.add_savings('WF Savings', 90000, 'retirement')
my_savings.delete_savings('Emergency Fund')