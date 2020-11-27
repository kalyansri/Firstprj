glb="sagar global"
class sag:
    classvar="Class variable"

    def __init__(self,name,empID):
        self.name=name
        self.empID=empID

    def opening_account(self,branch):
        print("The branch is {} and account is for {} and ID geertaed is {}".format(branch,self.name,self.empID))
        print(sag.classvar)  # class variable claaling
        print(globals()['glb']) #Global variables calling
        #x = math.sqrt(9)
        #print(x)


Obj=sag("Sagar",12345)
Obj.opening_account("Rajahmundry")