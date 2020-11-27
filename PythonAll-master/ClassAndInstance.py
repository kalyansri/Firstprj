# a.py
class A:
   message = "class message"

   @classmethod
   def cfoo(cls):
      print(cls.message)

   def foo(self, msg):
      self.message = msg
      print(self.message)


   def __str__(self):
      return self.message

n = A()
print(n)
n.foo('instance call')
A.foo(n,"Cll by using class name")
print(A.message)
A.cfoo()
def table(value):
    for s in range(1,13):

        print("{0} * {1} =".format(value,s), value*s)

table(int(input("Enter required table : ")))