def calculator(arg):
    def sum():
        return (a+b)
    def dif():
        return(a-b)
    def product():
        return(a*b)
    def fraction():
        return(a/b)    

    if arg==1:
        return sum()
    elif arg==2:
        return dif()
    elif arg==3:
        return product()
    else:
        return fraction()


a=int(input('Enter the number a: '))
b=int(input('Enter the number b: '))


print(calculator(int(input('Enter a number from 1 to 4: '))))
