# OOP - Encapsulation

# Define a class called BankAccount
class BankAccount:

    # Define a constructor method that takes a balance argument and sets it as a private attribute
    def __init__(self, balance):
        self.__balance = balance

    # Define a method called deposit that takes an amount argument and adds it to the balance attribute
    def deposit(self, amount):
        self.__balance += amount

    # Define a method called withdraw that takes an amount argument and subtracts it from the balance attribute
    # If the amount is greater than the balance, raise a ValueError with the message "Insufficient funds"
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    # Define a method called get_balance that returns the balance attribute
    def get_balance(self):
        return self.__balance
    
# Create a BankAccount object with an initial balance of 1000
account = BankAccount(1000)

# Try to withdraw 500 from the account
account.withdraw(500) # -> Decrease the balance by 500

# Try to withdraw 1000 from the account
account.withdraw(1000) # -> ValueError: Insufficient funds

# Try to deposit 200 into the account
account.deposit(200)

# Print the current balance of the account
print(account.get_balance())

# Try to access the balance attribute directly
print(account.__balance) # -> AttributeError: 'BankAccount' object has no attribute '__balance'
