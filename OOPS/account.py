class Account():

    # def __init__(self,name):
    #     self.account_type = name
        
    def account_name(self,name):
        return name

    def add_money(self,money):
        self.deposit = money

    def check_balance(self):
        return self.deposit
a = input("What type of account you want")
Aryaman = Account()
print("Your account is of type-->")
print(Aryaman.account_name(a))

print("how many money you want to add")
b = int(input("enter value"))

Aryaman.add_money(b)
print("Your current balance is-->")
print(Aryaman.check_balance())
