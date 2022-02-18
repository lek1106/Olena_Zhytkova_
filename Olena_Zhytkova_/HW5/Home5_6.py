positive=0
negative=0
while True:
    number=int(input('Enter the number: '))
    
    if number>0:
        positive+=1
        percentage_P=(positive/(positive+negative))*100
        print(f'Positive={percentage_P}%')    
    
    elif number<0:
        negative+=1
        percentage_N=(negative/(positive+negative))*100
        print(f'Negative={percentage_N}%') 
    
    else:
         break
     