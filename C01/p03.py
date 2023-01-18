#3.comprehensions

list1=[11,-21,0,45,66,-93]  #list numbers
positive=[pos for pos in list1 if pos>=0]
print("positive numbers:",positive)

n=int(input("\n enter the nth number:")) #SQUARE OF N NUMBERS
print("Square:",[s*s for s in range(1,n+1)])

def check_vow(string,vowels):  #vowels
    final=[each for each in string if each in vowels]
    print("\n total vowels: ",len(final))
    print(final,"\n")
string="geek  for geeks is doing good job"
vowels="AaEeIiOoUu"
check_vow(string,vowels)

word="hallucination" #ordinal
print("ordinal values:",[ord(s) for s in word])
