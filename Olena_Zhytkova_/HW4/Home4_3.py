number=int(input('Enter a number: '))
digit = 0
for i in str(abs(number)):
    digit += 1
    if number>0:
        sign='positive'
    elif number<0:
        sign='negative'  
    else:
        sign='Zero without sign positive/negative'   

dict={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}


print(f'{sign} {dict.get(digit)}-digit')


