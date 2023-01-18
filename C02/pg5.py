def contnum(n):
	for i in range(1, n+1):
 		num = i
 		digit = 1
 		for j in range(0, i):
 			print(num, end="\t")
 			digit = digit + 1
 			num = i * digit
 		print("\r")
n = int(input("enter a number:"))
contnum(n)
