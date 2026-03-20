print('Enter your age here: ')
age = int(input())
years_until = 18 - age
if age >= 18:
    print('You are of age and can drive')
else:
    print('Your are not of age to drive you are ',years_until,' years from driving')
    
my_age = 27
younger = my_age - age
older = age - my_age
if age < my_age:
    print('you are',younger ,'years younger then I am')
elif age > my_age:
    print('you are',older ,'years older then I am')
elif age == my_age:
    print('WOW we are the same age')
    
print('Enter your first number: ')
A = input()
print('Enter your second number: ')
B = input()
if A > B:
    print('A is greater then B')
elif A < B:
    print('A is less then B')
elif A == B:
    print('A is equal to B')
    
print('Enter your score here :')
score = int(input())
if score >= 80:
    print('You got an A')
elif score >= 70:
    print('You got an B')
elif score >= 60:
    print('You got an C')
elif score >= 50:
    print('You got an D')
else:
    print('You got an F')
    
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Enter a fruit: ')
guess = input()
if guess not in fruits:
    fruits.append(guess)
    print(fruits)
else:
    print(guess,'is already in list')
    
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

print(person.get('skills'))
print(person.get('skills')[2])
if 'python' in 'skills':
    print(person.get('skills'))

if 'skills' == 'JavaScript' and 'React':
    print('He is a front end developer')
elif 'skills' == 'Node' and 'Python'and 'MongoDB':
    print('He is a backend developer')
elif 'skills' == 'React'and'Node' and 'MongoDB':
    print('He is a fullstack developer')
else: 
    print('unknown title')
