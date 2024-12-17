class bankAccount:
  def __init__(self, account_holder, balance = 0):
    self.account_holder = account_holder
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    print(f"{amount} deposited and current New balance is  {self.balance}")
    
  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"{amount} withdraw and current new balance is {self.balance}")
    else:
      print("insufficient funds.")
      
account = bankAccount("Martin Githae", 2000000)

account.deposit(40000000)
account.withdraw(20000000)