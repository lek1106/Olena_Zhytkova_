radius_of_stage=int(input('Enter the radius of stage: '))
side_of_hall=int(input('Enter the side of square hall: '))
width_of_passage=int(input('Enter the width of passage: '))
if (side_of_hall-width_of_passage)>=radius_of_stage*2:
    poss='possible'
else:
    poss='unpossible'
print(f'With these radius, side and width it is {poss.capitalize()}.')        