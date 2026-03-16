import math
# I imported math to get best square rooting 
#1.
age = 27 
#2.
height  = 0,75
#3.
complex_number = 1 + 3j 

#4.
print("area of triangle")
print("Enter your base here: ")
base = int(input())
print("Enter your height here: ")
height = int(input())
area_triangle = 0.5 * base * height
print("The area of your triangle is",area_triangle) 

#5.
print("Perimeter of triangle")
print("Enter side A of triangle")
side_A = input()
print("Enter side B of triangle")
side_B = input()
print("Enter side C of triangle")
side_C = input()
perimeter_triangle = side_A + side_B + side_C
print("The perimeter of your triangle is",perimeter_triangle) 

#6.
print("rectangle calcultions")
print("Enter your base here: ")
length = int(input())
print("Enter your height here: ")
width = int(input())
area_rectangle = length * width
perimeter_rectangle = 2*(length + width)
print("The area of your rectangle is",area_rectangle)
print("The perimeter of your rectangle is",perimeter_rectangle)

#7.
print("circle calculations")
pi = 3.14
print("Enter your radius here: ")
radius = float(input())
print("The area of your circle is", float(pi) * radius * radius)
print("The circumfrense of your circle is", 2 *pi * radius)

print("mathematical graph theory")
#8.
#The variables marked with _8 stem from y = 2x-2
y1_8 = -2 
y2_8 = 0
x1_8 = 0
x2_8 = 1
#9.
#The variables marked with _8 stem from question 9 on Asabeneh's 30 day code challende day 3
y1_9 = 2
y2_9 = 10
x1_9 = 2
x2_9 = 6
slope_8 = m = y2_8-y1_8/x2_8-x1_8
Euclid_distance_8 = math.sqrt(((x1_8-x2_8)*(x1_8-x2_8))+((y1_8-y2_8)*(y1_8-y2_8)))
slope_9 = m = y2_9-y1_9/x2_9-x1_9
Euclid_distance_9 = math.sqrt(((x1_9-x2_9)*(x1_9-x2_9))+((y1_9-y2_9)*(y1_9-y2_9)))
print(slope_8)
print(slope_9)
print(Euclid_distance_8)
print(Euclid_distance_9)
#10.
print(slope_8 == slope_9) 

#11.
print("Calculating at what value y=0 in y = x^2 + 6x + 9")
print("x would have to be -2 because")
x = -3
y = (x*x) + (6*x) + 9
print("y = (-2)^2 + 6(-2) + 9")
print("y = 4 + (-12) + 9")
print("y = -12 + 12")
print("y =",y)

#12.
print("Comparative")
print("Python length is",len("python"))
print("Python length is",len("Dragon"))
print(len("python") == len("Dragon"))

#13
print('on' in "python" and  "on" in "dragon")

#14
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

#15
#Unclear instuctions
print("on" not in "dragon" and "python")

#16
float_check = float(len("python"))
str = str(float_check)
print(str)

#17
print("Enter your number to be checked by the even/odd detector :")
Even_number_attempt = float(input())
Even_number_checker = Even_number_attempt%2
print(Even_number_checker)
if Even_number_checker == 0:
    print("Even")
else:
    print("odd")

#18
int_check = 2.7
floor_division = 7//3 
print(int_check == floor_division)

#19
type("10")
type(10)
print(type("10") == type(10))

#20
#print(int('9.8') == 10)
#ValueError: invalid literal for int() with base 10: '9.8'

#21
print("Enter your Hours per week :")
Hours = int(input())
print("Enter your rate per Hour :")
rate = int(input())
print("Your weekly earning are",Hours*rate)

#22
print("Enter Number of years")
num_years = int(input())
if num_years < 100:
    print("This is how many seconds are in that many years",31536000 * num_years )
else:
    print("A person can't live that long")
    
#23
sequence_list = ["1 1 1 1 1","2 1 2 4 8","3 1 3 9 27","4 1 4 16 64","5 1 5 25 125"]
print(*sequence_list ,sep='\n',)