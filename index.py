class User:
    
    def __init__(self,name,email,account_balance):
        self.name = name
        self.email = email
        self.account_balance = BankAccount(int_rate = 0.02, balance = 0)
    
    def example_method(self):
        self.account_balance.deposit(100)
        print(self.account_balance)
        

class BankAccount: 
    
    def __init__(self,name,in_rate,account_balance):
        self.name = name
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

juanjose = User('Juan Jose','juanjose@hello.com')
print(juanjose)

# us = BankAccount('Juan Jose',0.02,100000)
# us.deposit()
# us.withdraw()
# us.display_account_info()

