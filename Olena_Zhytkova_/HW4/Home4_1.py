year=int(input('Enter a year: '))
if year %4 == 0:
    print('This year is intercalary.')
else:
    print('This year is not intercalary.') 
print('This year bilongs',int(year/100),'century.' )  

