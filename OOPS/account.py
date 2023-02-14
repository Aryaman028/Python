class Account():

    def __init__(self,name):
        self.account_type = name
        
    def account_name(self):
        return self.account_type

    def add_money(self,money):
        self.deposit = money
    def check_balance(self):
        return self.deposit

Aryaman = Account("Savings")
print(Aryaman.account_name)
Aryaman.add_money(3000)
print(Aryaman.check_balance())