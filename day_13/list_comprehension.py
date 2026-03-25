#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
below_1 =  [i for i in numbers if i < 1]
print(below_1)

#2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend_list = [number for row in list_of_lists for number in row]
print(flattend_list)

#3
numbers = [
    (num, *(num**i for i in range(7))) 
    for num in range(11)
]
for row in numbers:
    print(row)
#numbers = [(num, num * i) for i in range(11) for  num in range(11)]

#print(numbers)     
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

capitalized_country = [
    [country.upper(), country[:3].upper(), city.upper()] 
    for sublist in countries 
    for country, city in sublist
]

print(capitalized_country)

#5
keys = ['Finland','Sweden','Norway']
values = ['Helsinki','Stockholm','Oslo']
countries_dict = dict(zip(keys, values))
print(countries_dict)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

concatenate = [[name+" "+surname]
               for sublist in names 
               for name,surname in sublist
               ]
print(concatenate)
y = lambda m, x, c:  m * x + c 
print(y(3,2,5))