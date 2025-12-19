import time
# For loop
# Sart from 0, ends before range
for i in range(5) : print(i)
# Start from first number, ends before last number
for i in range(5, 10) : print(i)
# To solve the not printing last number (simply add 1)
for i in range(100, 105+1) : print(i)
# Add increment or decrement as the third parameter
for i in range(1,20,2) : print(i)
# For strings
for i in "Adib Chowdhury" : print(i)
# Reverse for
for i in range(10,3,-1) : print(i)

# Happy Birthday Countdown
for i in range(10, 0, -1) : 
    print(i)
    time.sleep(1)

print("Happy Birthday Man!")