def fibonacci_function(n):
    f1=f2=1 
    print(f1,f2,end=' ') 
    for i in range(1,n):
        f1,f2=f2,f1+f2
        print(f2,end=' ')

fibonacci_function(int(input('Enter the number: ')))       
