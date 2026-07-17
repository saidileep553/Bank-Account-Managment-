class BankAccount:
    def __init__(self, account_num, holder_name, balance):
        self.account_num= account_num
        self.holder_name = holder_name
        self.balance = balance

    def checking_balance(self):
        print("\nCurrent Balance:",self.balance)

    def deposit(self,amount):
        self.balance+= amount
        print("Amount Deposited sucessfully")
        print("Current Balance:",self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print("Amount Debited sucessfully")
            print("Current Balance:",self.balance)

        else:
            print("Sorry Insufficient amount/balance.")

account = BankAccount(1001, "Sai", 23000)

while True:
    print("\n= BANK ACCOUNT MANAGEMENT SYSTEM =")
    print("1. checking_balance Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.checking_balance()

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 3:
        amount = int(input("Enter amount to do  withdraw: "))
        account.withdraw(amount)

    elif choice == 4:
        print("Thank you for using our Bank Account Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")
