import math

def second_dimension_euclidean():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    d = math.sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))
    return d, x1, y1, x2, y2


def third_dimension_euclidean(x1, y1, x2, y2):
    print("Enter number for z1:")
    z1 = float(input())
    
    print("Enter number for z2:")
    z2 = float(input())
    
    Euclid = math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))+((z2-z1)*(z2-z1)))
    return Euclid

d, x1, y1, x2, y2 = second_dimension_euclidean()

if d < 0:
    print("not allowed check your numbers again")
print(d, "cm")
print(round(d), "cm")

print("Do you need 3D Distance (Y/N):")
fork_in_road = input().lower()

if fork_in_road != "y":
    print("ok guess not!")
else:
    Euclid = third_dimension_euclidean(x1, y1, x2, y2)
    print(Euclid, "cm")
    print(round(Euclid), "cm")
