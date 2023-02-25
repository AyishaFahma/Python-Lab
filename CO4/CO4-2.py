class bank_account():
    def _init_(self,ac_no,n,tacc):
        self.ac_number=ac_no
        self.name=n
        self.type=tacc
        self.balance=0
        print("\n\nHello!!! Welcome to the Deposit & Withdrawal Bank")
    def deposit(self):
        amount = float(input("\nEnter an Amount to Deposit : "))
        self.balance=self.balance+amount
        print("\nAmount deposited is : ",amount)
        print("After Transaction Account Balance is : ",self.balance)
    def withdraw(self):
        wamount=float(input("\n\nEnter an Amount to Withdraw : "))
        if (self.balance >= wamount):
            self.balance=self.balance-wamount
            print("\nAmount Withdraw is : ",wamount)
            print("After Transaction Account Balance is : ",self.balance)
        else:
            print("\nInsufficient balance")
            print("Your Account Balance is : ",self.balance)
    def details(self):
        print("\n\nHolder's Account Details")
        print("Account Number : ",self.ac_number)
        print("Name : ",self.name)
        print("Account Type : ",self.type)
        print("Balance : ",self.balance)
ac_no=int(input("Enter Account Number : "))
n=input("Enter Account Holder's Name : ")
tacc=input("Enter Account Type : ")
acc=bank_account(ac_no,n,tacc)
acc.deposit()
acc.withdraw()
acc.details()
