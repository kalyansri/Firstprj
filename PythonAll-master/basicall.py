x=0


while(x<=10):
    print(f"{x}is less than 10")
    x += 1
    if x==3:
        continue
    print(x)

# Checking string functions

SS="sagar learnig python"

if  SS.endswith("on"):
    print("Present")
else:
    print("Not present")

# for d in SS.split(" "):
#     if d=="python":
#         print("python is present")
#
#     else:
#         print(f"not present im {SS}")