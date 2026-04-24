# Similar to list and set, but tuple is Ordered, Unchangeable, duplicate elements are allowed, and FASTER
names = ("adib", "jamil", "adib", "chowdhury", "hossain")

# length
print(len(names))

# check if the element is there
print("chowdhury" in names)
print("khan" in names)

# index
print(names.index("jamil"))

# count
print(names.count("adib"))

# apply for loop
for name in names : print(name)