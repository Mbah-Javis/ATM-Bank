
from bank import Bank
from account import Account

bank_list = [Bank("1", "Afriland First Bank", ["Base", "Premium", "Gold", "Diamond"]),
Bank("2", "CCA Bank", ["Base", "Premium", "Gold"]),
Bank("3", "UBA Bank", ["Base", "Premium", "Diamond"]),
Bank("4", "NFC Bank", ["Base", "Premium", ])]

def welcome_menu():
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


def selectBank(option):
    if (option < (len(bank_list))):
        return bank_list[option]
    return ValueError("Invalid bank selected")

def selectBankOption(option):
    match option:
        case 0:
            return None
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

def displayBankMenu():
    print('--> 0. Go back')
    print('--> 1. Crate a bank account')
    print('--> 2. Deposit into an account')
    print('--> 3. Withdraw from account')
    print('--> 4. View transaction history')
    
welcome_menu()
