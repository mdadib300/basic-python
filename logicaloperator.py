# Logical Operator (and, or, not)
temp = int(input('Enter the temperature: '))
if (temp>=0 and temp<=30) : 
    print("Temperature is okay, go outside.")
else : print("Stay home")

age = int(input("Enter your age "))
money = int(input("Enter your money "))
if age<40 or money>50000 : print("I love youuuuu")
else : print("Mommyyyyyyy! Help me from this giant!") 

hedom = int(input("If you have hedom type 1 otherwise 0: "))
if not(hedom==1) : print("Tomar to miya hedom e nai! bhodai")
elif not(hedom==0) : print("Bah! tomar to dekhi valoi hedom!")