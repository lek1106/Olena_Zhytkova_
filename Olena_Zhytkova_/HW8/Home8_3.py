def month_check(month):
    """This function checks if entered date month is bitween  1-12,
     because Gregorian calendar include twelve months"""
    if 1 <=month <=12: 
        return True
    else:
        return False    
        
def day_check(month,day,year):
    """This function checks number of days in each month,
     returns 29 day in Fabruary for a leap year."""

    days_of_month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} 
    
    if (year%4==0 and year%100!=0) or year%400==0:
        days_of_month[2]=29
    else:    
        days_of_month[2]=28   
        
    if 1<=day<=days_of_month[month]:
        return True
    
    else:
        return False   
            

def year_check(year):
    if 0<year<=9999:
        return True
    else:
        return False    


def date_function():
    """Input the date and check it,
    then print result"""
    date=input('Enter the date in dd/mm/yyyy format:')
    day,month,year=date.split('/')
    if month_check(int(month)) and day_check(int(month),int(day),int(year)) and year_check(int(year)):
        print(f'The {date=} is IN Gregorian calendar!')
    else:
        print(f'The {date=} is OUT of Gregorian calendar!')    

date_function()        
