from numbers import Number
from string import punctuation
tup = (1,2,8,47,35,'j','frfg','A','G','2','F','=', '[', '{', '~', '+', '@', '/', '\\', '?', '(',\
     ':', '$', '.', '}', '*', ';', '#', '%', ',', '`', '!', ']', '<')
set_punctuation={'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',',\
     '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
l_number=[]
l_str=[]
l_object=[]
for x in tup:
    if isinstance(x, Number):
        l_number.append(x)
    elif isinstance(x,str):
        if x in set_punctuation:
            l_object.append(x)    ;
        else:    
            l_str.append(x)
        
print(tuple(l_number))
print(tuple(l_str))
print(tuple(l_object))   


