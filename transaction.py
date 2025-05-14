import datetime
import json
import os
from bank import Bank
from account import Account

def loadDatabase(path):
    db_path = os.path.join("db", path, "transactions.json")
    if os.path.exists(db_path):
        with open(db_path, 'r') as file:
            return json.load(file)
    else:
        print("Error loading accounts")
        return {}

def saveDatabase(data, path):
    db_path = os.path.join("db", path, "transactions.json")
    with open(db_path, 'w') as file:
        json.dump(data, file, indent=4)

class Transaction(object):
    def __init__(self, amount, type, id = None):
        self.amount = amount
        self.type = type
        self.id = id if id is not None else self.generateTransactionId()
        self.date = str(datetime.datetime.now(datetime.timezone.utc))

    def generateTransactionId(self):
        """Generates a random 10-digit transaction ID."""
        import random
        return str(random.randint(1000000000, 9999999999))
    
    def addBankAccountInfo(bank: Bank, account: Account):
        bank_transactions = loadDatabase(bank.db_path)
        bank_transactions[account.account_number] = {}
        saveDatabase(bank_transactions, bank.db_path)
    
    def addTransaction(self, bank: Bank, account: Account):
        """Add new bank transaction"""
        key = self.id
        transaction = {
            "id": key,
            "amount": self.amount,
            "type": self.type,
            "date": self.date
        }
        bank_transactions = loadDatabase(bank.db_path)
        account_transactions = bank_transactions.get(account.account_number, None)
        account_transactions[key] = transaction
        saveDatabase(bank_transactions, bank.db_path)
    
    def getAccountTransactions(bank: Bank, account: Account):
        """Get bank account transactions"""
        bank_transactions = loadDatabase(bank.db_path)
        account_transactions = bank_transactions.get(account.account_number)
        return account_transactions
