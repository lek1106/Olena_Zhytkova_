number_of_place=int(input('Enter the number of a place (1-54): '))
if number_of_place%2 !=0:
    place="bottom"
else:
    place='top'
if number_of_place<=36:
    side="compartment"
else:
    side="side"
print(f'This number of a place is {place} {side}.')    
