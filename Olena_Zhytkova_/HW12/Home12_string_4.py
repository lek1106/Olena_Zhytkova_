import re  
    
text=input('Enter the text: ')
total=0
spaces=re.findall('\s+',text)

for i in range(0,len(spaces)):
    print(len(spaces[i]))
    total += len(spaces[i])

print (f'There are {total} spaces in text.') 