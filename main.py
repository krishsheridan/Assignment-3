class Account:  
    def __init__(self, id, name, rate, funds):
        # Initialize account with id, owner's name, interest rate, and starting funds
        self.id = id
        self.name = name 
        self.rate = rate 
        self.funds = funds 

    def balance(self):
        # Return the current balance of the account
        return self.funds
    
    def modify_funds(self, amount):
        # Modify the funds of the account (add or subtract)
        self.funds += amount

class Savings(Account):
    
    def __init__(self, id, name, rate, funds, limit):
        # Initialize savings account with a minimum balance limit
        super().__init__(id, name, rate, funds)
        self.limit = limit

    def transaction(self, amount):
        # Process transactions ensuring the balance does not fall below the minimum limit
        if self.funds - amount >= self.limit:
            self.funds -= amount
            return "Transaction complete."
        return "Transaction failed: Insufficient funds."
    
class Checking(Account):
    
    def __init__(self, id, name, rate, funds, credit):
        # Initialize checking account with a credit limit
        super().__init__(id, name, rate, funds)
        self.credit = credit 

    def transaction(self, amount):
        # Process transactions considering the credit limit
        if self.funds + self.credit - amount >= 0:
            self.funds -= amount
            return "Transaction complete."
        return "Transaction failed: Credit limit reached."
    
class Bank:
    
    def __init__(self):
        # Initialize bank with an empty list of accounts
        self.registry = []

    def account_search(self, id):
        # Search for an account in the registry by id
        return next((acc for acc in self.registry if acc.id == id), None)
    
    def setup(self):
        #Account(number, name, interest, starting balance, minimum balance)
        self.registry.append(Checking("1", "Barry", 0.03, 1500, 500))
        self.registry.append(Savings("2", "Aura", 0.5, 3000, 1000))
        self.registry.append(Checking("3", "Chunglee", 0.13, 2000, 500))
        self.registry.append(Savings("4", "Peely", 0.01, 4000, 1000))
        self.registry.append(Checking("5", "Julian", 52.0, 2500, 500))

class BankSystem:
    
    def __init__(self, bank):
        # Initialize the banking system with a bank instance
        self.bank = bank
        self.bank.setup()

    def display_main_menu(self):
        # Display the main menu and handle user interaction
        while True:
            print("Bank System Main Menu")
            print("[1] Access Account")
            print("[2] Shutdown")

            option = input("Select an option: ")
            if option == "1":
                self.access_account()
            elif option == "2":
                print("System Shutdown")
                break

    def access_account(self):
        # Access an account using its ID
        id = input("Enter Account ID: ")
        account = self.bank.account_search(id)
        if account:
            self.account_operations(account)
        else:
            print("Account not found.")

    def account_operations(self, account):
        # Display account operations menu and handle user interaction
        while True:
            print(f"\nOperations for {account.name}'s Account")
            print("[1] Show Balance")
            print("[2] Deposit Money")
            print("[3] Withdraw Money")
            print("[4] Return to Main Menu")

            operation = input("Select an operation: ")
            if operation == "1":
                output = f"Balance: ${account.balance()}"
                print(output)
            elif operation == "2":
                amount = float(input("Deposit Amount: "))
                account.modify_funds(amount)
                print("Deposit succesful.")
            elif operation == "3":
                amount = float(input("Withdraw Amount: "))
                output = f"{account.transaction(amount)}New Balance: ${account.balance()}"
                print(output)
            elif operation == "4":
                break

def initiate_system():
    # Initialize and start the banking system
    institution = Bank()
    system = BankSystem(institution)
    system.display_main_menu()

initiate_system()

