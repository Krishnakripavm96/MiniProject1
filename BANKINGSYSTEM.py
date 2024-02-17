def accountlogin():
    x=int(input("Enter the account number:"))
    y=input("Enter your Name: ")
    input("BranchCode:")
    w=int(input("Enter your Mobile Number:"))
login=accountlogin()
print(login)
print("Account login successfully")
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to Deposit & WithdrawalMachine")
    def deposit(self):
        amount = float(input("Enter the amount to be deposited"))
        self.balance+=amount
        print("Amount Deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn:"))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdraw:",amount)
        else:
            print("Insufficient Balance")
    def display(self):
        print("Net Available Balance=",self.balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
