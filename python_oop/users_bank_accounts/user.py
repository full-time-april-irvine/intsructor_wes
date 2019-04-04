from bank_account import BankAccount

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

if __name__ == "__main__":
    wes = User('Wes', 'wharper@codingdojo.com')
    wes.display_user_balance()