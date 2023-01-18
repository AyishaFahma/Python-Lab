def add_string(str1):
 if str1[-3:] == 'ing':
     str1 += 'ly'
 else:
     str1 += 'ing'
 return str1
print(add_string('b'))
print(add_string('ic'))
print(add_string('string'))
