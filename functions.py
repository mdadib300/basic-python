# Function - block of code which can be reused by calling it
def sum(n1, n2) : return n1+n2 # the function
print(sum(40, 50)) # it is function calling

# set default value of an parameter, but the value will be changed if we set argument value
def net_price(tag_price, discount=0, tax=0.05): return tag_price*(1-discount)*(1+tax)
print(net_price(1000))

# even if the order is not maintained, the function will work respectively due to keyword arguments
def greet(text, title, first, last): print(f"{text}, {title} {first} {last}.")
greet('Hello', 'Mr.', 'Adib', 'Chowdhury')
greet('Hello', 'Mr.', 'Chowdhury', 'Adib') # Problems is shown here
greet('Hello', 'Mr.', last='Chowdhury', first='Adib') # Solves the issue here

# pass tuple as an argument
def showList(*args): 
    for arg in args: print(arg)
showList(2, 3, 4, 5, 8)

# pass dictionary as an argument
def address(**kwargs):
    for value in kwargs.values() : print(value)
address(street='123 True road', village='Abdullahpur', upazilla='Keraniganj', zilla='Dhaka')
