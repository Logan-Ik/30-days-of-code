from collections import Counter
from day_14.countries_data import data_set
#1
def add_two_numbers ():
    num1 = 12
    num2 = 13
    sum = num1 + num2
    print(sum)
add_two_numbers()

#2
def area_of_circle (r):
    PI = 3.14
    area = PI* r ** 2
    return area
print(area_of_circle(90))

#3
def add_all_nums(*args):
    sum = 0
    for num in args:
        if not isinstance(num,(int, float)):
            return ('Numbers are the only option here bucko')
        sum += num     
    return sum
print(add_all_nums(2, 1, 2, 3)) 
print(add_all_nums(2, "hello", 3)) 

#4
def temp_conversion (C):
    F = (C*9/5)+ 32
    return F
print(temp_conversion(3))
    
#5
def check_season(month):
    
    month = month.lower()
    
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'That is not a valid month, bucko!'


print(check_season('October')) 
print(check_season('june'))    

#6
def return_slope(x2,x1,y1,y2):
    cordinate_X = x2 - x1 
    cordinate_Y = y2 - y1
    m = cordinate_Y/cordinate_X
    return m
print(return_slope(12,3,1,2))

#7
def quadratic_equation (a,b,c):
    x = (-b + ((b**2)-4*a*c)**0.5)/2 
    x_2 = (-b - ((b**2)-4*a*c)**0.5)/2
    
    #This was the vision however it gets way to complicated for a simple excercise
    #quadratic_equation = a*(x-x_2)**2 + b*x + c 
    #expected = 0
    #assert quadratic_equation == expected, f"Calculation failed: Expected {expected}, got {quadratic_equation}"
    
    return x,x_2
print(quadratic_equation(1,2,3))

#8
def print_list (*args):
    for prints in args:
        print(prints)
        
    return prints 
print(print_list(1,2,3,4,5,6,7,8))

#9
def reverse_list(*args):
    for order in args:
        reverse = order[::-1]
        print(order)
        
    return reverse
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"])) 

#10
def capitalise_list_items(list_items): 
    result = [] 
    
    for word in list_items:
        capitalised = word.upper()
        result.append(capitalised) 
        
    return result 

my_list = ['this', 'is', 'capitalised']
print(capitalise_list_items(my_list))

#11
def add_item(list_items, item_to_add): 
    result = list(list_items) 
    result.append(item_to_add)
    return result 

my_list = ['this', 'is', 'capitalised']
print(add_item(my_list, 'not'))
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))   

#12
def remove_item(list_items, item_to_remove): 
    result = list(list_items) 
    result.remove(item_to_remove)
    return result 
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#13
def sum_of_numbers(num):
    total = 0
    for i in range(0,num + 1,1):
        total += i
        
    return total
print(sum_of_numbers(5))  
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

#14
def odds(num_odd):
    total = 0
    for i in range(0,num_odd,2):
        total += i
        
    return total
print(odds(5))  
print(odds(10)) 
print(odds(100))

#15
def even(num_even):
    total = 0
    for i in range(0,num_even,1):
        if i % 2 != 0:
            total += i
        
    return total
print(even(5))  
print(even(10)) 
print(even(100))

#Excercise level 2

#1
def evens_and_odds(num):
    evens = 0
    odds = 0
    
    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1  
        else:
            odds += 1   
            
    return (f"The number of odds are {odds}.\nThe number of evens are {evens}.")

print(evens_and_odds(100))

#2
def factorial (num):
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact

print(factorial(5))

#3
def calculate_mean(nums):
    return sum(nums) / len(nums)

def calculate_median(nums):
    ordered = sorted(nums)
    n = len(ordered)
    mid = n // 2
    
    if n % 2 == 0:
        return (ordered[mid - 1] + ordered[mid]) / 2
    else:
        return ordered[mid]
    
def calculate_mode(list_items):
    data = Counter(list_items)
    return data.most_common(1)[0][0]

def calculate_variance(nums):
    mean = calculate_mean(nums)
    sum_sq_diff = sum((x - mean) ** 2 for x in nums)
    return sum_sq_diff / len(nums)

def calculate_std(nums):
    variance = calculate_variance(nums)
    return variance ** 0.5

colour_list = ['Red', 'Blue', 'Red', 'Green', 'Red', 'Blue']

#4 
def greet(name):
    if len(name) < 1:
        print("Hello, Guest!")
    else:
        print('Hello,',name,'!') 
print(greet(""))
print(greet('jordan'))

#5
def show_args(**args):
    proof = args
    return proof
print(show_args(name="Alice", age=30, city="New York"))
print(show_args(name="Bob", pet="Fluffy, the bunny"))
#excercise 3
#1
def is_prime(num):
    if num <= 1:
        print(False)
    else:
        is_prime = True 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    return is_prime
print(is_prime(float(input())))

#2
def unique(items):
    return len(items) == len(set(items))

print(unique(['Red', 'Blue', 'Red', 'Green', 'Red', 'Blue']))

#3
def same_type (items):
    return type(items) == type(set(items))
print(unique(['Red', 'Blue', 'Red', 'Green', 'Red', 'Blue']))

#4
def error_check(error):
    try:
        result = 10 / error
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    print("Program continues here.")
    return result
#5
def something():
    languages = set()

    for data in data_set:
        languages.update(data['languages'])
    all_languages = []
    for country in data_set:
        all_languages.extend(country['languages'])


    counts = Counter(all_languages)

    print(counts.most_common(10))
    
def get_population(country):
    return country['population']

data_set.sort(key=get_population, reverse=True)

top_ten = data_set[:10]


for country in top_ten:
    print(country['name'], country['population'])