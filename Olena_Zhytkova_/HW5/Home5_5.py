P=10
H=15
sum=0
product=1
n=0
while True:
    number=int(input('Enter the number: '))
    if number==P or number==H:
        print(number)
        break
    elif number<P:
        sum+=number 
        print(f'Suma: {sum}')
    elif number>H:
        product*=number
        print(f'Product: {product}')    
        
    else:
        for i in range(P,H+1):
            if number==i:
                print(f'Number in range: {number}')
            

            
                   
                