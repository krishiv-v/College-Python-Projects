class bankaccount:
    def __init__(self, account_number , balance= 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your account balance is {self.balance}")
        else:
            print("Sorry, you cannot deposit money.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Your account balance is {self.balance}")
        else:
            print("Sorry, you cannot withdraw money.")

    def check_balance(self):
        print(f"Account balance is {self.balance}")

account = bankaccount("BCD140768",4000)
account.deposit(250)                                           #deposited
account.withdraw(5000)                                         #withdraw
account.check_balance()