money=int(input('Enter the amount of money: '))
banknotes=[200,100,10,1]
banknotes_200=int(money/200)
if money % 200 != 0:
    rest_money_200=money-200*banknotes_200
else:
    rest_money_200=0    
banknotes_100=int(rest_money_200/100)
if rest_money_200 % 100 != 0:
    rest_money_100=rest_money_200-100*banknotes_100
else:
    rest_money_100=0
banknotes_10=int(rest_money_100/10) 
if rest_money_100 % 10 != 0:
    rest_money_10=rest_money_100-10*banknotes_10
else:
    rest_money_10=0
coin=int(rest_money_10)               


print('200 banknotes:',banknotes_200,'---','100 banknotes:',banknotes_100,'---' ,'10 banknotes:', banknotes_10,'---','1 UAH coin:',coin) 
      
