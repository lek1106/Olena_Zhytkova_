def prime_function(a):
    """If number is simple it has only two divisors 1 and itself.
    iterate over the numbers, starting from 2,
    until we find the divisor of the our number.
    If this divisor is our number, then number is simple."""
    div=2
    while a%div !=0:
        div+=1
    return div==a
            
  
result=prime_function(a=int(input('Enter the number from 0 to 1000: ')))  
print('The number is simple - ',result)      