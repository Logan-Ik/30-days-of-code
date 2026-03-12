import math
addition = (3+4)
subtraction = (3-4)
multiplication = (3*4)
modulus = (3%4)
division = (3/4)
exponential = (3**4)
Floor_division_operator = (3//4)     
print(addition,
      subtraction,
      multiplication,
      modulus,
      division,
      exponential,
      Floor_division_operator)
name = "Bob"
family_name= "TheBuilder"
country = "Somewhere"
statment = "I am enjoying 30 days of python"
int = 6
tuple = ["orange","banana","mango"]
def fruit(apple,banana):
      apple = apple
      banana = banana
 
print(name,family_name,country,statment,"            ",int,tuple)
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh','Python','Finland']))
print(type(name))
print(type(family_name))
print(type(country))
print(type(tuple))
print(type(int))
print(type(fruit))
print("Enter number for x1:")
x1 = float(input())
print("Enter number for y1:")
y1 = float(input())
print("Enter number for x2:")
x2 = float(input())
print("Enter number for y2:")
y2 = float(input())
p=(x1*x1 - y1*y1) 
print(p) 
ptrue = math.sqrt(p)
print(ptrue)
q=(x2*x2 - y2*y2)
print(q)
qtrue = math.sqrt(q)
print(qtrue)
d = (ptrue + qtrue)
print(d,"cm")
print(round(d),"cm")
