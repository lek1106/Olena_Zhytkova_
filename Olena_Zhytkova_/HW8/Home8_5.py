def year_leap_function(year):
    """This function checks if the year is high,
    if year is leap, than True,
    else - False."""
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False
result=(year_leap_function(int(input('Enter the year in format yyyy: '))))  
print('This year is high - ', result)  
print(year_leap_function.__doc__)        