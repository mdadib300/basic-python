# Calculate the area of a circle
pi = 3.141625987156849819354
radius = input("Enter the raidus of the circle: ")
radius = float(radius)
print(f"The area of the circle is: {round(pi*radius*radius, 2)}")
# Python does not support multiplication of different data types, so I changed the data type of radius to float from int cause pi is in float.
# The area takes too many decimal places due to pi, so I rounded the area to 2 decimal places using round()


# c = Root over (a^2 + b^2)
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = math.sqrt(pow(a,2)+pow(b,2))
print(f"C = {c}")

# Decide if a person is voter or not
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if (age>=18) : print(f"{name} is elligible to be a voter")
elif (age<0) : print(f"Let {name} born first!")
else : print(f"{name} is not elligible to be a voter")