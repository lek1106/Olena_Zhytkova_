Salad_tuna_avocado=['Yogurt','Tuna','Rice','Pea','Red pepper','Avocado','Lime']
Healthy_salad=['Potato','Eggs','Bean','Tomato','Anchovies','Tuna','Mayonnaise']
Warm_salad=['Mushrooms','Mustard','Red pepper','Onion','Lentil','Olive oil','Cheese']
Fish_with_pea=['Fish','Peas','Onion','Olive oil','Cream']
def lettuce_decorator(func):
    def wrapper():
        func()
        print('Lettuce')
        print('-' * 30)
    return wrapper 

@ lettuce_decorator
def Fish_with_pea():
    print('"Fishwith pea" ingredients:')
    print('Fish')
    print('Peas') 
    print('Onion')
    print('Olive oil')
    print('Cream') 

@ lettuce_decorator
def Healthy_salad():
    print('"Healthy salad" ingredients:')
    print('Potato')
    print('Eggs') 
    print('Bean')
    print('Anchovies')
    print('Tuna')     
    print('Mayonnaise') 

@ lettuce_decorator
def Warm_salad():
    print('"Warm salad" ingredients:')
    print('Mushrooms')
    print('Lentil') 
    print('Mustard')
    print('Red pepper')
    print('Olive oil')     
    print('Cheese')
    print('Onion') 

@ lettuce_decorator
def Salad_tuna_avocado():
    print('"Salad tuna avocado" ingredients:')
    print('Tuna')
    print('Rice') 
    print('Yogurt')
    print('Red pepper')
    print('Pea')     
    print('Avocado')
    print('Lime')     

Fish_with_pea() 
Healthy_salad()
Warm_salad()
Salad_tuna_avocado()