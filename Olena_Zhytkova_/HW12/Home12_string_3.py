def Product(number):
    product_digits=1
    temp=number
    while temp!=0:
        product_digits *= temp%10
        temp=int(temp/10)

    print(product_digits) 



def ProductReverse(rev_digits):
    product_reverse=1
    temp=rev_digits
    while temp !=0:
        product_reverse *=temp%10
        temp=int(temp/10)
    print(product_reverse)

if __name__=='__main__':
    try:
        number=int(input('Enter the number: '))
        rev_digits=int(str(number)[::-1])

    except ValueError: 
        print('Given input is not a number! Please try again.')  

    try:
        Product(number)
        ProductReverse(rev_digits)
    except NameError:
        print('Please try again \'Enter the number\'.')    

