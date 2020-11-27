

file=open("ss.txt", 'r')

print(file.readline())

fie=open("ss.txt", 'a')

sti="i love python"
fie.write(sti)
fie.close()

file=open("ss.txt", 'r')
print(file.readline())

