list_1=list()
list_2=list()
a=input("enter no of elements for list_1:")
for i in range(0,int(a)):
    list_1.append(int(input("value for list_1:")))
print(list_1)
b=input("enter no of elements for list_2")
for i in range(0,int(b)):
    list_2.append(int(input("value for list_2:")))
print(list_2)
if len(list_1)==len(list_2):
    print("the list are equal in length")
else:
    print("the list are unequal in length")


print(sum(list_1))
print(sum(list_2))
if sum(list_1)==sum(list_2):
    print("list sums are equal")
else:
    print("list sums are not equal")

    
common=[num for num in list_1 if num in list_2]
if len(common)!=0:
    print("these are the common element",common)
else:
    print("there are no common elements:")

