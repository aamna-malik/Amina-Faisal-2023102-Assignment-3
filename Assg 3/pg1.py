class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal: -${amount}")
                return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
            else:
                return "Insufficient funds. Withdrawal failed."
        else:
            return "Invalid withdrawal amount. Please enter a positive value."

    def balance_inquiry(self):
        return f"Current balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history


# Example usage:
account = BankAccount("John Doe", 1000)

print(account.balance_inquiry())

print(account.deposit(500))
print(account.withdraw(200))
print(account.balance_inquiry())

print(account.withdraw(1500))  # Should display an error message
print(account.deposit(-200))   # Should display an error message

print("Transaction History:")
print(account.get_transaction_history())
