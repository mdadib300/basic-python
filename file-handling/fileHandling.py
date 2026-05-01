# Till now we were storing data in variables that means in the Code. But in real life the data are stored in txt, csv, or json formatted file. Reading, replacing or adding more data in the existing file are defined as file handling (Read, Write, Append). 

# Types of file is added in the folder (txt, csv [For ML])

# Reading a file
with open("data.csv", "r") as lotsOfData: # with -> open this file and automatically close 
    data = lotsOfData.read()
print(data) # Run code from bash like this => cd file-handling => python fileHandling.py

# Reading a file line by line
with open("data.csv", "r") as daata : 
    for datum in daata: print(datum)

# Writing a file (Replace old text with new one)
with open("data.txt", "w") as info:
    info.write("I replaced all the old text with this.")
# Now checking
with open("data.txt", "r") as editedInfo:
    editedData = editedInfo.read()
print(editedData)

# Appending new lines
with open("data.txt", "a") as addedInfo: 
    addedInfo.write("\n New line added!")
# Checking
with open("data.txt", "r") as editedInfo:
    editedData = editedInfo.read()
print(editedData)
