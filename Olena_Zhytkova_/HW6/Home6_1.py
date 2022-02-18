from random import randint
n=int(input('Enter the len of list: '))

random_list=[randint(0,100) for j in range(n)]
keyboard_list=[int(input('Enter:')) for i in range(n)]
third_list=[x+y for x,y in zip(random_list,keyboard_list)]

print(random_list)
print(keyboard_list)
print(third_list)