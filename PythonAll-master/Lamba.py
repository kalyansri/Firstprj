from functools import *

lab=lambda a,b:a*b
print(lab(2,3))

# Map is that it loops all the elements in list by specified function
n={2,3,4,5,6}
mp=list(map(lambda a:a*2,n))

print(mp)

# Reduce will consolidate all the elents and ive one value
red =reduce(lambda a,b:a+b,mp)

print (red)

#Filter the list based on filter condition

fil=list(filter(lambda a:a%2==0,n))
print(fil)

week=["sat", "Mon", "sat"]
ch=list(filter(lambda l:l=="sat",week))
print(ch)