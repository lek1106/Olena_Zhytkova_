def arithmetic_function(a,b,c):
    """This function 
    add two arguments if third argument '+'
    substract if third argument '-'
    multiply if third argument '*'
    divide first to second if third argument '/'"""
    if c=='+':
        res=a+b
        return(res)
    elif c=='-':
        res=a-b
        return(res)
    elif c=='*':
        res=a*b
        return(res)
    elif c=='/':
        res=a/b
        return(res)
    else:
        return('Unknown operation') 
result=arithmetic_function(int(input('First: ')),int(input('Second: ')),input('Third: '))        
print(result)   
print(arithmetic_function.__doc__)                       