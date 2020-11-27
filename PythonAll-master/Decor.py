def div(a,b):
    return a/b


#decorator
def smart(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return fun(a,b)
    return inner


print(div(1,4))
div=smart(div)

print(div(2,4))


