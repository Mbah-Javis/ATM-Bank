class Account(object):
    def __init__(self, name, email, phone_number, pin, account_type, balance = 0.0, account_number = None):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.pin = pin
        self.account_type = account_type
        self.balance = balance
        self.account_number = account_number if account_number is not None else self.generateAccountNumber()

    def generateAccountNumber(self):
        """Generates a random 10-digit account number."""
        import random
        return str(random.randint(1000000000, 9999999999))
    
    def getBalance(self):
        """Returns the current balance."""
        return self.balance
    
    def getName(self):
        """Returns the current name."""
        return self.name
    
    def getPin(self):
        """Returns the current PIN."""
        return self.pin
    
    def getAccountType(self):
        """Returns the current account type."""
        return self.account_type
    
    def getAccountNumber(self):
        """Returns the current account number."""
        return self.account_number
    
    def getEmail(self):
        """Returns the current email."""
        return self.email
    
    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        print(self.balance)
        self.balance = float(self.balance) + (amount)
        return None
    
    def withdraw(self, amount):
        """Withdraws the given amount."""
        if amount < 0:
            return "Amount must be >= 0"
        elif float(self.balance) < amount:
            return "Insufficient funds" 
        else:
            self.balance = float(self.balance) - amount
            return None
