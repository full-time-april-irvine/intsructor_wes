class BankAccount:
    def __init__(self, interest_rate, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate

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
        print(f"Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100}%")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

ba = BankAccount(0.01)
ba2 = BankAccount(0.01)

ba.deposit(10).deposit(10).deposit(10).withdraw(5).yield_interest().display_account_info()

ba2.deposit(10).deposit(10).withdraw(30).withdraw(30).withdraw(30).withdraw(30).yield_interest().display_account_info()