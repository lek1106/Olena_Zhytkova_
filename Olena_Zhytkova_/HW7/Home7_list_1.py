from random import randint
n=int(input('Enter the len of list: '))
random_list=[randint(1,100) for a in range(n+6)]
keyboard_list=[int(input('Enter the number:')) for b in range(n)]
third_list=[a+b for a,b in zip(random_list,keyboard_list)]

print(random_list)
print(keyboard_list)
print(third_list)