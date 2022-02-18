lenght=int(input('Enter the lenght: '))
width=int(input('Enter the width: '))
for i in range(width+1):
    if i==0 or i==(width):
        for j in range(lenght+1):
            print('-',end=' ')
    else:
        print('|',end=' ')
        for j in range(1,lenght):
            print('*',end=' ')  
        print('|',end=' ')        
    print()  

    