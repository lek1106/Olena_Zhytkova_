import math
def area_function(arg):
    arguments=list(arg.split(','))
    print(arguments)
    if len(arguments)==1:
        area=math.pi * int(arg)**2
        print(f'Area of circle is {area:>20}.')
    if len(arguments)==2:
        area=int(arguments[0])* int(arguments[1])  
        print(f'Area of rectangle is {area:>8}.')
    if len(arguments)==3:
        p=(int(arguments[0])+int(arguments[1])+int(arguments[2]))/2
        area=(p*(p-int(arguments[0]))*(p-int(arguments[1]))*(p-int(arguments[2])))**0.5 
        print(f'Area of triangle is {area:>20}.') 
area_function(input('Enter the number: '))        
  