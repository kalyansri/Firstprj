name="sagar"

print(f"the name is is :{name}")
print("Another method of format {}".format(name))
print("Place holder of String with number : {1} and {0}" .format('sagarNCR','Vidyasagar'))
# Creating file
va="sagar new file is created \n"

try:
    file1=open(r"C:\Users\Va185060\Desktop\Knowledge\Python\FilePro\MyFile.txt","a+")
    file1.write(va)
    file1=open(r"C:\Users\Va185060\Desktop\Knowledge\Python\FilePro\MyFile.txt","r+")

    print(file1.read())

except:
    print("An exception occured during opening")

finally:
    print("finally block executed")
    file1.close()
