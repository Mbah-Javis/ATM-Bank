class Bank(object):
    def __init__(self, id, name, account_types = None):
        if (account_types == None):
            return "Account types must be a list with any of this types [Base, Premium, Gold, Diamond]"
        else:
            self.id = id
            self.name = name
            self.account_types = account_types
    
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