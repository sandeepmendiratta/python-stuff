class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f" Account Owner: {self.owner} \n Account balance: ${self.balance}"

    def deposite(self,dep_amt):
        self.balance += dep_amt
        print(f" ${dep_amt} added to te the account,new total: ${self.balance}")

    def withdraw(self,draw_amt):
        if self.balance > draw_amt:
            self.balance = self.balance - draw_amt
            print(f" {draw_amt} from balance {self.balance}")
        else:
            print(" Sorry, not enough money in the account")

acct1 = Account("Jose",100)
print(acct1)
acct1.deposite(100)
acct1.withdraw(200)
