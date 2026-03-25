from functools import reduce
from countries import Countries
from countries_data import data_set
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1
diffrences = """
                The diffrence between map,filter and reduce is that 
                map transforms each element,
                filter selects an element based on a condition and
                reduce accumulates elements based into a single value
            """

#2
differentials = """
                The diffrence between higher order functions, closures and decorators is
                A higher order function is a broad programming concept 
                while closures are a specific mechanism that allows inner functions to remeber their surrounding state 
                and decprators are a specific application that typically uses closures and specisal syntax to modify other functions behaviours 
                """
explanations = diffrences,differentials
print(explanations)

#3
def call_test (num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(call_test, numbers)
print(list(even_numbers))   

#4
for country in countries:
    print(country)
    
#5
for number in numbers:
    print(number)
    
#Excercise 2
#1
def change_to_upper(country):
    return country.upper()

upper_country = map(change_to_upper, countries)
print(list(upper_country))    

#2
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

#3
def change_name_upper(name):
    return name.upper()

upper_country = map(change_to_upper, names)
print(list(upper_country))  

#4
def no_land(country):
    if 'land' not in country:
        return True
    return False
no_land_act = filter(no_land,countries)
print(list(no_land_act))

#5
def six_flags(name):
    if len(name) == 6:
        return True
    return False
no_long_names_I_get_jelous = filter(six_flags,countries)
print(list(no_long_names_I_get_jelous))

#6
def not_long(name):
    if len(name) < 6:
        return True
    return False
no_long_names_I_get_jelous = filter(not_long,countries)
print(list(no_long_names_I_get_jelous))

#7
def no_E_scape(i):
    if 'E' not in i:
        return True
    return False
E_mansipated = filter(no_E_scape,countries)
print(list(E_mansipated))

#8    
def no_land(country):
    if 'land' not in country:
        return True
    return False
no_land_act = list(map(str.upper, filter(no_land, countries)))
print(list(no_land_act))

#9
def get_strings(ls_str):
    return [i for i in ls_str if isinstance(i, str)]
string = get_strings(countries)

print(string)

#10
def number_sum(x, y):
    return int(x) + int(y)

total = reduce(number_sum, numbers)
print(total)   

#11
def countries_concat(x, y):
    return x +', '+y

total = reduce(countries_concat, countries)
print(total, 'are north European countries')     

#12
def categorize_countries(Country):
    if 'land' in Country:
        return True
    return False
land_Countries = filter(categorize_countries,Countries)
print(list(land_Countries))

#13
keys = [word[0] for word in Countries]
values = Countries
countries_dict = dict(zip(keys, values))
print(countries_dict)

#14
def get_first_ten_countries():
    return Countries[:10]

print("First Ten:", get_first_ten_countries())
#15
def Final_ten():
    return Countries[-10:]

print("Last Ten:", Final_ten())

#Excercise 3

#i
all_names = []
all_population = []
all_capital = []
for country in data_set:
    all_names.append(country['name'])
    all_population.append(country['population'])
    all_capital.append(country['capital'])
print(all_capital,all_names,all_population)

#ii
def most_spoken_language(country):
    return country['languages']

data_set.sort(key=most_spoken_language, reverse=True)

top_ten = data_set[:10]


for country in top_ten:
    print(country['name'], country['languages'])
    
#iii
def most_popular_city(country):
    return country['population']

data_set.sort(key=most_popular_city, reverse=True)

top_ten = data_set[:10]


for country in top_ten:
    print(country['name'], country['population'])