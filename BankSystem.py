class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    
    def deposit (self,amount):
        self.balance += amount
    def get_balance (Self):
        return Self.balance
    
    def withdraw (self,amount):
        if amount <= self.balance:
         self.balance -= amount

        else:
            print("Insufficient Funds brodah!")

account = BankAccount ("Fidel", 400)    

account.get_balance()

        
account.deposit(200)
account.withdraw(100)

print(account.get_balance())