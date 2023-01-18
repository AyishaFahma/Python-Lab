#6.store list of first names

fNames=["syed","adam","philip","narayanan"]
count=0
for x in fNames:
    for y in x:
        if y=='a':
            count+=1
print("'a' has occured",count,"times")
