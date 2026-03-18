#1 and 2
def dog(name, 
        color, 
        breed, 
        legs, 
        age):
    name='gromit' 
    color='white'
    breed='a Beagle'
    legs='two legs'
    age= 6
    print(name,color,breed,legs,age)    
#3
student = {'first_name':'first_name', 
           'last_name':'last_name', 
           'gender':'gender', 
           'age':'age',
           'marital status':'marital status',
           'skills':['html'],
           'country':'country',
           'city':'city',  
           'address':'address'}
#4
print(len(student))

#5
print(student.get('skills'))
print(type(student.get('skills')))

#6
student['skills']= 'HTML','Python'
print(student.get('skills'))

#7
keys = student.keys()
print(keys)

#8
value = student.values()
print(value)

#9
print(student.items())
student.pop('age')
print(student)

#10
del dog
#print(dog)
#If this print is run then it will give error dog is not defined since dog gone