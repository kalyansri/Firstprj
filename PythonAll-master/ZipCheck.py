tup1=("sag","allu","Vidya")
tup2=("dev","tester","sdet")

# maps two tupples and gives as single zip object
# we can convert to anynumber of format dir set etc
ziplist=list(zip(tup1,tup2))
print(ziplist)
zipped=zip(tup1,tup2)

for (a,b) in zipped:
    print(a,b)