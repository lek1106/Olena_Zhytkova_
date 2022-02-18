my_collections_of_marks={'cats':['red','orange','black','red','black'],
'cars':[1,2,3,4,5],
'elephants':[['african','african' ],'indian']}
another_collections_of_marks={'bycicles':[1,2,3,4,8]}

print(list(my_collections_of_marks.items()))

#міняємо колекцію машинок на колекцію мотоциків
del my_collections_of_marks['cars']
print(list(my_collections_of_marks.items()))
 
my_collections_of_marks={**my_collections_of_marks,**another_collections_of_marks}
print(list(my_collections_of_marks.items()))

#для унікальних марок з колекції котів
cats=['red','orange','black','red','black']
print(set(cats))

