n=1
count=0
while n<=10:
    number=int(input('Enter the number:  '))
    if number>2:
        if number%5==0:
            count+=1
        n+=1        
    else:
        print('The number must be greater than 2!')        
    
print(count)    
        


