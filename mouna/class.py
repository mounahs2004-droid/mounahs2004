#class and objects
#Bank Account Simulator

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

# Create account
acc = BankAccount("John", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)
