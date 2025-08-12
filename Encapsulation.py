class BankAccount:
    def __init__(self, owner , balance):
        self.owner = owner
        self._balance = balance
    
    def deposit(self,amount):
        self._balance  += amount

    def get_balance(self):
        return self._balance
    
acc = BankAccount("Fidel", 100)
acc.deposit(40)

print(acc.get_balance())


