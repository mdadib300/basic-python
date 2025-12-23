# List means Array
friends = ["Adib", "Badib", "Cadib", "Dadib"]

# Access list element: listName[index]
print(friends[0])
# Modify list element: 
friends[3] = "Rod Ridoy"
# Append element: add element to the end of the list
friends.append("Eadib")
# Remove element
friends.remove("Badib")
# Pop: removes the last element
friends.pop()
# Insert: Insert new element at any index
friends.insert(3, "Gobinda")
# Sort: alphabatically
friends.sort()
# Clear
friends.clear()

# Print list elements using loop
for i in friends : print(i)