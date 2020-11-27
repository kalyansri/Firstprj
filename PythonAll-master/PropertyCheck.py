class PropCheck():

    def __init__(self,dd,temperature=0):
        self._temperature=temperature
        self._dd=dd

    @property
    def temperature(self):
         print("printting geter method")
         return self._temperature

    @temperature.setter
    def temperature(self,value):

        print("temperature setter is printing")
        self._temperature=value

p=PropCheck(100)
print(p.temperature)
p.temperature=200
print(p.temperature)