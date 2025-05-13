
from bank import Bank
from account import Account

bank_list = [Bank("1", "Afriland First Bank", ["Base", "Premium", "Gold", "Diamond"]),
Bank("2", "CCA Bank", ["Base", "Premium", "Gold"]),
Bank("3", "UBA Bank", ["Base", "Premium", "Diamond"]),
Bank("4", "NFC Bank", ["Base", "Premium", ])]

def welcomeMenu():
    selected_bank = None
    print("\n--- Welcome to SIU ATM ---")
    print('Chose a bank below to proceed\n')
    for i in range(len(bank_list)):
        print(f"--> {i}. {bank_list[i].name}")
    print('\n')
    select = int(input("Select bank: "))
    selected_bank = selectBank(select)
    print(f"Selected bank: {selected_bank.name}")
    displayBankMenu()
    option = int(input("Select an option: "))
    selectBankOption(option, selected_bank)

def selectBank(option):
    if (option < (len(bank_list))):
        return bank_list[option]
    return ValueError("Invalid bank selected")

def createBankAccount(bank):
    print(f"\nCreate {bank.name} account")
    name = input("--> Enter your full name: ")
    email = input("--> Enter your email: ")
    phone_number = input("--> Enter your phone number: ")
    pin = int(input("--> Enter a 4 digit PIN to protect your account: "))
    confirm_pin = int(input("--> Confirm PIN: "))
    if pin == confirm_pin:
        new_account = Account(name, email, phone_number, pin)
        Bank.addAccount(bank, new_account)
        print(f"\n--> Account number: {new_account.account_number}")
    else:
        print("--> PIN does not match")

def depositIntoAccount(bank):
    print(f"Selected bank: {bank.name}")
    pass

def withdrawMoney(bank):
    print(f"Selected bank: {bank.name}")
    pass

def viewTransactionHistory(bank):
    print(f"Selected bank: {bank.name}")
    pass

def selectBankOption(option, bank):
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

def displayBankMenu():
    print('--> 0. Go back')
    print('--> 1. Crate a bank account')
    print('--> 2. Deposit into an account')
    print('--> 3. Withdraw from account')
    print('--> 4. View transaction history')
    
welcomeMenu()
