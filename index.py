class BankAccount: 
    
    def __init__(self,username,in_rate,account_balance):
        self.name = username
        print("Hello Welcome", self.name,"to the banck account", account_balance)

    def deposit(self):
        amount = float(input("Enter amount to be deposite: "))
        self.account_balance =+ amount
        print("Amount deposite:", amount)
        print(self.account_balance)

    def withdraw(self):
        amount = float(input("Enter amount to be withdraw: "))
        if self.account_balance >= amount:
            self.account_balance -= amount
            print("Amount withdraw:", amount)
        else:
            print("Insufficent balance")

    def display_account_info(self):
        print("Your balance account:", self.account_balance)

    def yiel_interest(self):
        pass

user = BankAccount('Juan Jose',0.02,100000)
user.deposit()
user.withdraw()
user.display_account_info()