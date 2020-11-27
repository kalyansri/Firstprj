from threading import *
from time import sleep
class sag(Thread):

    def run(self):
        for i in range(5):

            print("hi first")
            sleep(1)


class two(Thread):

    def run(self):
        for i in range(5):

            print("hi")
            sleep(1)

a=sag()
b=two()
a.start()
sleep(.2)
b.start()

x=4
print("if loop") if x>5 else print("Else block")