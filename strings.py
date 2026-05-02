# String is so much important for NLP (NLP = 80% String)
# Basic operations (Upper, Lower, Split)
# address = input('Type your full address: ')
address = "Keraniganj, Dhaka"
# To upper case
print(address.upper())
# To lower case
print(address.lower())
# To split the phrase or sentence by words (whitespaces)
print(address.split())
# To split the phrase or sentence by anything you want (ex.- with fullstop (.))
print(address.split('.')) # It will return a list

# Replace one thing with other
name = "Md. Adib Chowdhury" # We'll replace the fullstop with empty string
print(name.replace(".", "")) 

# Check if the thing is there or not (Returns True or False)
print("Chowdhury" in name)
print("Khan" in name)

# Check count() function