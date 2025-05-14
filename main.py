
from bank import Bank
from account import Account

bank_list = [Bank("1", "Afriland First Bank", "afriland", ["Base", "Premium", "Gold", "Diamond"]),
Bank("2", "CCA Bank", "cca", ["Base", "Premium", "Gold"]),
Bank("3", "UBA Bank", "uba", ["Base", "Premium", "Diamond"]),
Bank("4", "NFC Bank", "nfc", ["Base", "Premium"])]

def welcomeMenu():
    selected_bank = None
    print("\n--- Welcome to SIU ATM ---")
    print('Chose a bank below to proceed\n')
    for i in range(len(bank_list)):
        print(f"--> {i}. {bank_list[i].name}")
    print('\n')
    select = int(input("Select bank: "))
    selected_bank = selectBank(select)
    if selected_bank == ValueError:
        print("--> Invalid bank selected")
        return
    displayBankMenu(selected_bank)

def selectBank(option):
    if (option < (len(bank_list))):
        return bank_list[option]
    return ValueError("Invalid bank selected")

def createBankAccount(bank: Bank):
    print(f"\nCreate {bank.name} account")
    account_types = bank.getAccountTypes()
    print("Which account type do you want to create?")
    for i in range(len(account_types)):
        print(f"--> {i}. {account_types[i]}")
    print('\n')
    selectedIndex = int(input("--> Select account type: "))
    account_type = account_types[selectedIndex]
    if account_type == None:
        print("--> Invalid account type selected")
        return
    print(f"--> Selected account type: {account_type}")
    name = input("--> Enter your full name: ")
    email = input("--> Enter your email: ")
    phone_number = input("--> Enter your phone number: ")
    pin = int(input("--> Enter a 4 digit PIN to protect your account: "))
    if len(str(pin)) != 4:
        print("--> PIN must be 4 digits")
        return
    confirm_pin = int(input("--> Confirm PIN: "))
    if pin == confirm_pin:
        new_account = Account(name, email, phone_number, pin, account_type)
        bank.addAccount(new_account)
        print(f"\n--> Account created with {bank.name} successfully")
        print(f"--> Account name: {new_account.name}")
        print(f"--> Account email: {new_account.email}")
        print(f"--> Account number: {new_account.account_number}")
        print('\n')
        displayBankMenu(bank)
    else:
        print("--> PIN does not match")
        return

def depositIntoAccount(bank: Bank):
    print(f"Deposit into {bank.name} account")
    account_number = input("--> Enter your account number: ")
    account = bank.getAccount(account_number)
    if account == None:
        print("--> Account not found")
        return
    print(f"--> Account name: {account.name}")
    amount = float(input("--> Enter amount to deposit: "))
    if amount <= 0:
        print("--> Amount must be greater than 0")
        return
    account.deposit(amount)
    print(f"--> {formatAmount(amount)} deposited into account {account_number}")
    bank.updateAccount(account)
    bank.saveAccounts()
    print(f"--> New balance: {formatAmount(account.getBalance())}")
    displayBankMenu(bank)

def withdrawMoney(bank: Bank):
    print(f"Withdraw money from {bank.name} account")
    account_number = input("--> Enter your account number: ")
    account = bank.getAccount(account_number)
    if account == None:
        print("--> Account not found")
        return
    print(f"--> Account name: {account.name}")
    amount = float(input("--> Enter amount to withdraw: "))
    if amount <= 0:
        print("--> Amount must be greater than 0")
        return
    withdrawal_limit = bank.getWithdrawalLimit(account.getAccountType())
    if amount > withdrawal_limit:
        print(f"--> Amount exceeds withdrawal limit of {withdrawal_limit}")
        return
    if amount > account.getBalance():
        print(f"--> Insufficient funds. Current balance: {account.getBalance()}")
        return
    pin = int(input("--> Enter your PIN: "))
    if pin != account.getPin():
        print("--> Invalid PIN")
        return
    account.withdraw(amount)
    print(f"--> {formatAmount(amount)} withdrawn from account {account_number}")
    bank.updateAccount(account)
    bank.saveAccounts()
    print(f"--> New balance: {formatAmount(account.getBalance())}")
    displayBankMenu(bank)

def formatAmount(amount):
    return f"{amount:,.2f} XAF"

def viewTransactionHistory(bank: Bank):
    print(f"Selected bank: {bank.name}")
    pass

def selectBankOption(option, bank: Bank):
    match option:
        case 0:
            welcomeMenu()
        case 1:
            createBankAccount(bank)
        case 2:
            depositIntoAccount(bank)
        case 3:
            withdrawMoney(bank)
        case 4:
            viewTransactionHistory(bank)
        case _:
            raise ValueError("Invalid Option selected")

def displayBankMenu(bank: Bank):
    print(f"\nWelcome to {bank.name}")
    print('--> 0. Go back')
    print('--> 1. Crate a bank account')
    print('--> 2. Deposit into an account')
    print('--> 3. Withdraw from account')
    print('--> 4. View transaction history')
    option = int(input("Select an option: "))
    selectBankOption(option, bank)
    
welcomeMenu()
