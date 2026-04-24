# Similar to list but it is unordered, no duplicate elements

# Simply - set
set1 = {3, 4, 2, 5, 3, 12}
print(set1)

# Set from a list
numbers = [1, 2, 3, 4, 5]
set2 = set(numbers)
print(set2)

# add an element in the set
set2.add(45)
print(set2)

# remove an element from the set - will show an error if the element is missing
set1.remove(3)
print(set1)

# remove an element from the set with discard - it won't show any error even if the element is missing 
set1.discard(234556)
print(set1)

# Union set
print(set1.union(set2))

# intersection set
print(set1.intersection(set2))