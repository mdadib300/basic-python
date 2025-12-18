# Check if a person is voter or not
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if (age<0) : print("You have to at least born first to be a voter idiot!")
elif (age<18) : print("You are not elligible to be a voter")
else : print("Hmmmmm...You can vote")