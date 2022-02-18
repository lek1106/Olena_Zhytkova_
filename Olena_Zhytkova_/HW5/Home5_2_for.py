count=0
for i in range(10):
    number=int(input('Enter the number:  '))
    if number>2:
        if number%5==0:
            count+=1
               
    else:
        print('The number must be greater than 2!')        
    
print(count)    
        


