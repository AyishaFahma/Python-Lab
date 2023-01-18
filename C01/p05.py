#5.prompt the user for list of integer

it100=list()
num_int=1
while num_int!=0:
    num_str=input("input as integer(0 terminates):")
    num_int=int(num_str)
    if num_int<100:
        it100.append(num_int)
    else:
        it100.append("over")
print(it100)

#6.store list of first names

fNames=["syed","adam","philip","narayanan"]
count=0
for x in fNames:
    for y in x:
        if y=='a':
            count+=1
print("'a' has occured",count,"times")
