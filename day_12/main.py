from mymodulus import generate_full_name
from math import *
from statistics import *
from random import randint
import random
import string 

#1
r = random.choice(string.ascii_letters)
n = random.choice(string.digits)

user_id = n + r + r + n + n + r
print(user_id)

#2
def user_id_gen_by_user(length, amount):
    rlng = string.ascii_letters + string.digits
    ids = []

    for i in range(amount):

        new_id = ''.join(random.choice(rlng) for _ in range(length))
        ids.append(new_id)
    return "\n".join(ids)

print('Enter length of random code and how many you wish to generate:')

try:
    l = int(input("Length: "))
    a = int(input("Amount: "))
    print(user_id_gen_by_user(l, a))
except ValueError:
    print("Please enter numbers only!")

#3
def rgb_color_gen():
    rgb = randint(0,255),randint(0,255),randint(0,255)
    return rgb
print('rgb:',rgb_color_gen()) 

#Excercise 2

#1
def list_of_hexa_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
        
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)
print("hexa colour",list_of_hexa_colors())

#2
def list_of_rgb_colors(amount):
    all_colors = [] 
    for _ in range(amount):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colour = f"rgb({r}, {g}, {b})"
        all_colors.append(colour) 
    return all_colors 
print(list_of_rgb_colors(3))

#3
def generate_colors(mode, amount):
    colors = []
    
    for _ in range(amount):
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        if mode == 'hexa':
            color = '#{:02X}{:02X}{:02X}'.format(r, g, b)
        elif mode == 'rgb':
            color = f"rgb({r}, {g}, {b})"
        else:
            return "Invalid mode! Use 'hexa' or 'rgb'."
        colors.append(color)
    return colors

print("Hex 3:", generate_colors('hexa', 3))
print("Hex 1:", generate_colors('hexa', 1))
print("RGB 3:", generate_colors('rgb', 3))
print("RGB 1:", generate_colors('rgb', 1))

#Excercise 3

#1
def shuffle_list(my_list):

    random_ls = random.sample(my_list, len(my_list))
    return random_ls

print(shuffle_list(['bread', 'wheat', 'bacon']))
    
#2
def seven_nation_numbers():
    
    num = random.sample(range(0,9),7)
    return num

print(seven_nation_numbers())