def Caesar_encrypt(text,key):
    text_Caesar=""
    for i in text:
        if i.isupper():
            temp=65+((ord(i)-65+key) % 26 )
            text_Caesar+=chr(temp) 
        elif i.islower():
            temp=97+((ord(i)-97+key) % 26) 
            text_Caesar+=chr(temp)   
        else:
            text_Caesar += i
    print(text_Caesar) 

key=4
text=input('Enter the text: ')
Caesar_encrypt(text,key)

   
