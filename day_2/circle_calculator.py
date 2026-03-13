print("Enter your radice here: ")
r = float(input())
pi = 3.14159
area_of_circle= pi*(r*r)
circumfrence_of_circle = 2*pi*r
sphere_Volume = 1.33333333333*pi*(r*r*r)
surface_area = 4*pi*(r*r)

print("The area of your circle is :",area_of_circle)
print("The area of your circle(rounded) is :",round(area_of_circle))
print("The circumfrence of your circle is :", circumfrence_of_circle)
print("The circumfrence of your circle(rounded) is :",round(circumfrence_of_circle))

print("Do you need Sphere volume? (Y/N):")
fork_in_road = input().lower()
if fork_in_road != "y":
    print("ok guess not!")
else:
    print("The Volume of your sphere is :",sphere_Volume,)
    print("The Volume of your sphere(rounded) is :",round(sphere_Volume))
    

print("Do you need Surface Area? (Y/N):")
fork_in_road = input().lower()
if fork_in_road != "y":
    print("ok guess not!")
else:
    print("The surface area of your sphere is :",surface_area)
    print("The surface area of your sphere(rounded) is :",round(surface_area))


