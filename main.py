# This is Python Comment

# Start printing something
print("Hello World!")

# Getting started with variables 
# String
my_name = "Md. Adib Chowdhury"
print(my_name)
# Wanna play with print?
print(f"Bissash koren bhai, ami {my_name}")
# Integer
myAge = 21
print(f"My age is {myAge}")
# Float
myHeight = 5.5
print(f"My Height is not {myHeight}")
# Boolean 
isStudent = False
print(f"He is {isStudent}, he is not a student.")

# Conditional Statement (if else)
isRobber = False
if isRobber : print("He is robber")
else : print("He is not robber")

# Find the type of a variable [type(variableName)]
isTrue = False
print(type(isTrue))

# Change the type of a variable [typeOfToChanged(variableName)] [str(), int(), float(), bool()]
marks = 45
print(type(marks))
print(str(marks))
print(type(str(marks)))

# User input
# Input is stored as String data type
name = input("Type your name: ")
age = input("Type your age: ")
age = int(age)
age += 1
print(f"Your name is {name}")
print(f"You are {age} years old. The data type of age is {type(age)}.")

# Arithmatic Operators
number = 1
number = number + 1
number += 1

number = number - 1
number -= 1

number = number * 1
number *= 1

number = number / 1
number /= 1

number = number ** 1 
# It means power 

number = number % 1

# Mathematical functions
# round()
# abs() [makes a negative number positive]
# pow(2,3) [2^3]
# max(n1, n2, n3) [Will return the maximum number among n1, n2 and n3]
# min(n1, n2, n3) [Will return the minimum number among n1, n2 and n3]

# Things in math!
import math
print(math.pi)
print(math.sqrt(9))
# To round up a number [9.1 to 10]
print(math.ceil(9.1))
# To round down a number [9.9 to 9]
print(math.floor(9.9))