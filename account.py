class Account(object):
    def __init__(self, name, email, phone_number, pin, balance = 0.0):
        self.name = name
        self.email = email
        self.account_number = phone_number
        self.pin = pin
        self.balance = balance
        self.account_number = self.generateAccountNumber()
        self.transactions = {}

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
    
    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        self.balance += amount
        return None
    
    def withdraw(self, amount):
        """Withdraws the given amount."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds" 
        else:
            self.balance -= amount
            return None
    
    def generateTransactionId(self):
        """Generates a random 10-digit transaction ID."""
        import random
        return str(random.randint(1000000000, 9999999999))
    
    def addTransaction(self, transaction):
        """Add new bank transaction"""
        key = transaction.id
        self.transactions[key] = transaction