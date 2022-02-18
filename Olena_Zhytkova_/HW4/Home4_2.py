shape=str(input('Choose rectangle, triangle or circle: '))
if shape =='rectangle':
    height=int(input('Enter a height: '))
    weght=int(input('Enter width: '))
    area=height*weght
elif shape=='triangle':
    side1=int(input('Enter first side of triangle: '))   
    side2=int(input('Enter enother side of triangle: ')) 
    area=(side1*side2)/2
else:
    radius=int(input('Enter radius: '))   
    pi=3.14159
    area=pi*(radius**2)
print(f'The square of {shape} is ',area)