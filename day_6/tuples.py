import math
tpl = ()
#I will put my tools since I consider them my brothers and sisters
#1
brothers = ("Tom",'Scoop')
print(brothers)
#2
sisters = ('boppy','Dizzy', 'Roley')
print(sisters)
#3
siblings = brothers + sisters
print(siblings)
#4
print(len(siblings))
#5
parents = ('Robert','Dorothy')
family_members = siblings + parents
#Excercise 2
#1
sibs = len(family_members)-2
print(family_members[:sibs])
print(family_members[sibs:])
#2
vegetables = ('spinach','kale','carrots','potatoes','broccoli','cabbage')
fruit = ('apples', 'berries', 'citrus' ,'lemons', 'oranges', 'melons', 'peaches', 'plums')
animal_product = ('meat', 'dairy', 'eggs', 'honey','wool','leather', 'fur', 'silk','gelatin', 'tallow', 'rennet')
food_stuff_tp = fruit + animal_product + vegetables
print(food_stuff_tp)
#3
food_stuff_ls = list(food_stuff_tp)
#4
mid_food_stuff_upper = math.ceil(len(food_stuff_tp)/2)
mid_food_stuff_lower = math.floor(len(food_stuff_tp)/2)
print(food_stuff_tp[mid_food_stuff_lower:mid_food_stuff_upper])
#5
print(food_stuff_tp[0:3] , food_stuff_tp[22:26])
#6
del food_stuff_tp
#This command can not be printed since it will lead to unndefied name 
#print(food_stuff_tp)
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('Estonia is a nordic country')
else:
    print('Estonia is not a nordic country')
if 'Iceland' in nordic_countries:
    print('Iceland is a nordic country')
else:
    print('Iceland is not a nordic country')