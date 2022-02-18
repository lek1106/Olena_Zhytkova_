import random
number=random.randint(0,100)
n=1

while n<=10:
    guess=int(input('Guess the number: '))
    if guess<number:
        print('Too less!')
    elif guess>number:
        print('Too much!')
    else:
        print('You guess!')
        break
    n+=1 

else: 
    print(f'The number is {number}')          
