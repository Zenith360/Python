"""A Bank Account :)"""

class BankAccount(object):
  balance = 0;
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)
  def show_balence(self):
    print("%s's account. Balance: $%.2f" % (self.name, self.balance))
    self.start()
  def deposit(self, amount):
    if amount <= 0:
      print("Error");
      return;
    else:
      print("You are depostiting %.2f" % (amount))
      self.balance += amount
      self.show_balence();
      self.start()
  def withdraw(self, amount):
    if amount > self.balance:
      print("Error");
      return;
    else:
      print("You are withdrawing %.2f"% (amount));
      self.balance -= amount;
      self.show_balence();
      self.start()
  def start(self):
    while(True):
      ans = input("Welcome! This is your bank account! if you want to deposit something press\nlowercase d to withdraw to lower case w to see your balance do lower case b!\n Press lowercase e to exit!\n\n")
      if(ans == "d"):
        dep = int(input("Put the amount you wish to add!"));
        self.deposit(dep)
      if(ans == "w"):
        wit = int(input("Put the amount you wish to take away!"));
        self.withdraw(wit);
      if(ans == "b"):
        self.balance();
      if(ans == "e"):
        print("Goodbye!");
        return;
      else:
        print("I dont know what that is please try again!");


bank = BankAccount("James")
bank.start();