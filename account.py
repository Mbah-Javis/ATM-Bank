class Account(object):
    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.account_number = self.generateAccountNumber()

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