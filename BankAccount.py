class BankAccount:
    def __init__(self, name, balance): 
        self.name = name 
        self.balance = balance

    def __str__(self): 
        return ("Your bank name is" + self.name)
    
    def setBalance(self, balance): 
        self.balance = balance
    
    def checkBalance(self): 
        return ("Your current balance is " + str(self.balance)) 

    def deposit(self, amount): 
        self.balance = self.balance + amount
        return ("Your current balance after deposit is " + str(self.balance))
    
    def withdraw(self, amount): 
        self.balance = self.balance - amount
        return ("Your current balance after withdrawl is " + str(self.balance)) 
    

Bank = BankAccount("Bank of America", 0)
Bank.setBalance(15000)
print(Bank.checkBalance())
print(Bank.deposit(50))
print(Bank.checkBalance())
print(Bank.withdraw(500))
print(Bank.checkBalance())