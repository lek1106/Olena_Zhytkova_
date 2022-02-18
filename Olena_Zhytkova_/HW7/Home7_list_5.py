t=(1,2,3,4,5,6,7,8,9,0,
'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C',\
'V','B','N','M','a','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',\
'k','l','z','x','c','v','b','n','m','@','!','#','$','%','^','&','*','(',')','_','+','*',\
'/','-','+','|','?','>','<','.',',')

symbol=input('Enter a number, letter or special character from the keyboard: ')
if symbol=='1'or symbol=='2'or symbol=='3'or symbol=='4'or symbol=='5'or symbol=='6'or symbol=='7'\
    or symbol=='8'or symbol=='9'or symbol=='0':
    symbol=int(symbol);

if symbol in t:
    print(t.index(symbol))
else:
    print('Symbol is not in the tuple!')    
