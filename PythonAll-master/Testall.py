che=int(input("Enter number of columns"))

for row in range(1,che+1):
    for col in range(1,row+1):
        print(col, end=" ")
    print()
