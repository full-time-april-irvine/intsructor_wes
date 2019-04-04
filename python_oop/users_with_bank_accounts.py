class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest Rate: {self.int_rate * 100}%")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(int_rate=0.02, balance=0)]

    def make_deposit(self, amount, account=None):
        if account == None:
            account = self.accounts[0]
        account.deposit(amount)
        return self

    def make_withdrawal(self, amount, account=None):
        if account == None:
            account = self.accounts[0]
        account.withdraw(amount)
        return self
        
    def display_user_balance(self, account=None):
        if account == None:
            account = self.accounts[0]
        print(f"User: {self.name}, Balance: {account.balance}")
        return self

    def transfer_money(self, other_user, amount, account=None, other_account=None):
        if account == None:
            account = self.accounts[0]
        account.withdraw(amount)

        if other_account == None:
            other_account = other_user.accounts[0]
        other_account.deposit(amount)
        return self

wes = User("Wes", "wharper@codingdojo.com")
todd = User("Todd", "tenders@codingdojo.com")

wes.make_deposit(100)
wes.make_withdrawal(10)
wes.make_withdrawal(100)
wes.display_user_balance()