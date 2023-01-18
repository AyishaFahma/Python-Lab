Diction = {'red': '# FF0000', 'green': '# 00FF00', 'black': '# 000000', 'white': '# FFFFFF'}
print ("Sorted Dictionary :") 
for w in sorted (Diction, key = Diction.get):
	print (w, Diction[w])
print("Reverse Order :")
for w in sorted(Diction, key = Diction.get, reverse = True):
	print(w, Diction[w])
