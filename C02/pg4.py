l = int(input("Enter lower range: "))
u = int(input("Enter upper range: "))
a = [x for x in range(l,u+1) if (int(x**0.5))**2==x]
print("Perfect Squares are: \n",a)
e = []
for y in a:
 for s in str(y):
  if int(s)%2 != 0:
   break
 else:
   e.append(y)
print("Perfect Squares with only even digits are: \n",e)
