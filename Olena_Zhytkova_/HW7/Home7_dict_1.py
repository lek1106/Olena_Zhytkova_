string=str(input('Enter the text: '))
new_string=''
for x in range(len(string)):
    if string[x]!=string[(x-1)]:
        new_string+=string[x]

print(len(string))      
print(new_string)
print(len(new_string))        

