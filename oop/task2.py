class Account():
  def __init__(self,balance,account):
    self.balance = balance
    self.account = account

  # Debit 
  def debit(self,amount):
    self.balance -= amount
    print('Bdt ', amount , 'was debited from your account ',self.account , 'Your current balance is ',self.balance)

  def credit(self,amount):
    self.balance += amount
    print('Bdt ', amount , 'was credited from your account ',self.account , 'Your current balance is ',self.balance)

myAccount = Account(10000,'34353434')
myAccount.debit(2000)
myAccount.credit(2000)
myAccount.debit(5000)