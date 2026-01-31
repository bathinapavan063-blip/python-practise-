#print(ord("A"))
#print(chr(97))
#print(ord("D"))
'''
text = "devops"
for char in text:
    print(char,"->",ord(char))


'''
'''
ch="G"
if 65 <= ord(ch) <=90:
    print("ok")
else:
    print("NO")    
    '''
'''
ch="B"
if 65 <= ord(ch) <= 90:
    print("yes")
else:
    print("no")    
'''
text=65,67,90
ascii_values=[]
for value in text:
    ascii_values.append(chr(value))
print(ascii_values) 
   