class character:
 def __init__ (self,health,speed,damage):
  self.health = health
  self.damage = damage
  self.speed = speed

warrior = character(  100,70,20)
ninja = character(90,70,60)



print(f"warrior speed:{warrior.speed}")
print(f"ninja speed:{ninja.speed}")


class bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
         self.balance -= amount
        else:
           print("Insufficient funds!") 
    
account = bankaccount("Sandra", 2000)

account.deposit(300)
account.withdraw(200)

     