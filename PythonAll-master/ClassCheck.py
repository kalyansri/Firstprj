import time
class Bank(object):
    IFCCODE="TTM001"

    def __init__(self,account, type):
        self.account=account
        self.type=type



    def pr(self):
         print("the account is "+ self.account + "  "+ Bank.IFCCODE)

    def changBank(self,newBank):
        self.account=newBank
        print("the new bank which was changed by method is  " +self.account)
        print(time.asctime())




bk=Bank("HDFC","SAVINGS")
print(bk)
print(bk.account)
bk.account="ICICI"
print(bk.account)
bk.pr()
bk.changBank("AXIS")