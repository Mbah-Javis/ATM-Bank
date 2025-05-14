import json
import os
from account import Account

def loadDatabase(path):
    db_path = os.path.join("db", path, "accounts.json")
    if os.path.exists(db_path):
        with open(db_path, 'r') as file:
            return json.load(file)
    else:
        print("Error loading accounts")
        return {}

def saveDatabase(data, path):
    db_path = os.path.join("db", path, "accounts.json")
    with open(db_path, 'w') as file:
        json.dump(data, file, indent=4)

class Bank(object):
    def __init__(self, id, name, db_path, account_types = None):
        if (account_types == None):
            return "Account types must be a list with any of this types [Base, Premium, Gold, Diamond]"
        else:
            self.id = id
            self.name = name
            self.account_types = account_types
            self.db_path = db_path
            self.accounts = loadDatabase(self.db_path)
    
    def saveAccounts(self):
        """Saves the current accounts to the database"""
        saveDatabase(self.accounts, self.db_path)
        return None
    
    def getBankName(self):
        return self.name
    
    def getAccountTypes(self):
        return self.account_types
    
    def getWithdrawalLimit(self, type):
        match type:
            case "Base":
                return 100000
            case "Premium":
                return 200000
            case "Gold":
                return 300000
            case "Diamond":
                return 400000
            case _:
                raise ValueError("Invalid account type")
    
    def addAccount(self, account: Account):
        """Add new bank account"""
        key = account.account_number
        self.accounts[key] = {
            "name": account.name,
            "email": account.email,
            "phone_number": account.phone_number,
            "account_number": account.account_number,
            "pin": account.pin,
            "balance": account.balance,
            "account_type": account.account_type
        }
        self.saveAccounts()
    
    def removeAccount(self,  account_number):
        """Removes an account"""
        key = account_number
        self.accounts.pop(key, None)
        self.saveAccounts()
        return None

    def getAccount(self, account_number):
        """Returns an account with it's informations"""
        key = account_number
        account_data = self.accounts.get(key, None)
        if account_data:
            return Account(
                account_data["name"], 
                account_data["email"],
                account_data["phone_number"],
                account_data["pin"],
                account_data["account_type"],
                account_data["balance"],
                account_data["account_number"]
            )
        return None
    
    def updateAccount(self, account: Account):
        """Updates an account"""
        key = account.account_number
        self.accounts[key] = {
            "name": account.name,
            "email": account.email,
            "phone_number": account.phone_number,
            "account_number": account.account_number,
            "pin": account.pin,
            "balance": account.balance,
            "account_type": account.account_type
        }
        self.saveAccounts()
        return None
    