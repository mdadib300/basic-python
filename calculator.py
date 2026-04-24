operator = input("Enter the operator (+, -, /, *): ")
number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))

if (operator == '+') : print(number1+number2)
elif (operator == '-') : print(number1-number2)
elif(operator == '/') : print(number1/number2)
elif(operator == '*') : print(number1*number2)
else : print("Invalid Operator")