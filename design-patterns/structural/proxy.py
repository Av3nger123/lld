from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class RealBankAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}. Remaining balance: ${self.balance}")

# Extra function of authenticating is added an extension of Decorator Pattern
class BankAccountProxy:
    def __init__(self, real_account, password):
        self.real_account = real_account
        self.password = password

    def authenticate(self, password):
        return self.password == password

    def withdraw(self, amount, password):
        if self.authenticate(password):
            self.real_account.withdraw(amount)
        else:
            print("Access Denied! Incorrect password.")
            
if __name__ == "__main__":
    # Create a real bank account
    real_account = RealBankAccount(1000)

    # Create a proxy with password protection
    proxy_account = BankAccountProxy(real_account, "secure123")

    # Attempting to withdraw with correct and incorrect passwords
    proxy_account.withdraw(500, "wrongpass")  # Access Denied
    proxy_account.withdraw(500, "secure123")  # Successful withdrawal
    proxy_account.withdraw(600, "secure123")  # Insufficient balance
    
"""
Type of Proxy	 | Purpose	                   | Example
Virtual Proxy	 | Lazy loading to save memory | Image loading in a gallery
Protection Proxy | Restrict access	           | Bank account authentication
Remote Proxy	 | Access remote objects	   | Network communication
Caching Proxy	 | Store frequently used data  | API response caching
"""

