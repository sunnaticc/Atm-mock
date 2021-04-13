
class budget:
    def __init__(self, name):
        self.name=name
        self.legder=[]
    def Deposit(self, amount, description=""):
        self.legder.append(amount)
    def withdraw(self, amount, description=""):
        self.legder.append(-amount)
        
    def compute_balance(self):
        total_balance=0
        for item in self.legder:
            total_balance += item
        return total_balance
    def transfer(self, amount, category):
        self.withdraw(amount, "transfer to {}".format(category.name))
        category.Deposit(amount, "transfer to {}".format(self.name))

food=budget("food")
clothing=budget("clothing")
entertaiment=budget("entertaiment")

food.Deposit(1000)
food.withdraw(500)
entertaiment.Deposit(2000)
print(food.compute_balance())
food.transfer(100, clothing)
print(clothing.compute_balance())
print(food.compute_balance())
print(entertaiment.compute_balance())





