def bank_function(n,year):
    """ This function calculates the amount with 10%
    after a given number of years"""
    percent=10    
    for x in range(year):
        n=n+n*percent/100
    return(n)  
result=bank_function(float(input('Enter the sum of deposit: ')),int(input('Enter the years: ')))      
print(result)