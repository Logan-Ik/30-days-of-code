from countries import countries
from countries_data import data_set
from collections import Counter
#1
print('This is the for loop for #1')
numbers = (1,2,3,4,5,6,7,8,9,10)
for number in numbers:
    print(number)
print('This is the while loop for #1')
count = 0 
while count < 10:
    print(count)
    count = count+1
#2
print('This is the for loop for #2')
numbers_rev = (10,9,8,7,6,5,4,3,2,1)
for number in numbers_rev:
    print(number)
print('This is the while loop for #2')
count_rev = 10 
while count_rev > 0:
    print(count_rev)
    count_rev = count_rev-1
    
#3
hash = "#"
for i in range(1, 8):
    print(hash)  
    hash += "#"  
#4
hash_tag = ('#'' ''#'' ''#'' ''#'' ''#'' ''#'' ''#'' ''#'' ')
for i in range(1,9):
    print(hash_tag)
    
#5
for i in range(0,11):
    sum = i * i 
    print(i,"X",i ,"=",sum*1)
    
#6
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in languages:
    print(language)
    
#7
for i in range(0,101,2):
    print(i)
    
#8
for i in range(101):  
    if i % 2 != 0:    
        print(i)     
        
#Excercise 2
total = 0
for i in range(0,101,1):
    total += i
    print('The sum of all numbers is',total)

#2
total = 0
for i in range(0,101,2):
    total += i

total_odd = 0
for i in range(101):  
    if i % 2 != 0:  
        total_odd  += i
        print('The sum of all evens is',total,'. And the sum of all odds is',total_odd)
        
#Excercise 3
#1
countries = countries
search = "land"

for country in countries:
    if search in country:
        print(country)
        
#2
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in reversed(fruits):
    print(i)

#3i
languages = set()

for data in data_set:
    languages.update(data['languages'])

print("Total number of languages: ", len(languages))
#3ii
all_languages = []
for country in data_set:
    all_languages.extend(country['languages'])


counts = Counter(all_languages)

print(counts.most_common(10))
#3ii
def get_population(country):
    return country['population']

data_set.sort(key=get_population, reverse=True)

top_ten = data_set[:10]


for country in top_ten:
    print(country['name'], country['population'])