# Input: a sentence  
# Output: number of words
anySentence = "So what can be done if he does not come for the betterment of his own machine which was bought 20 years ago without any cash payment by which we could have get 10 percent discount."
def wordsOfASentence(sentence) : 
    listOfWords = sentence.split()
    wordCount = len(listOfWords)
    print(wordCount) 

wordsOfASentence(anySentence)

# Input: list of numbers  
# Output: list of squares
numbers1 = [2, 3, 4, 5]
def toSquare(numbers) : 
    sqNumbers = []
    for number in numbers : 
        result = sqNumbers.append(number * number)
        return result
print(toSquare(numbers1))

# Text cleaning
text = "I LOVE Python!!!"
print(text.lower().replace("!", ""))

# Count how many times a word appears
text = "I love ML and I love AI"
print(text.count("love"))

# Create a new list with only even numbers
list1 = [1, 2, 3, 4, 5, 6]
list2 = []
for num in list1 : 
    if(num%2==0) : list2.append(num)

print(list2)

# Find the average without using built-in functions like sum()
nums = [10, 20, 30, 40]
lengthOfNums = len(nums)
sumOfNums = 0
for num in nums : sumOfNums = sumOfNums + num
averageOfNums = sumOfNums / lengthOfNums
print(averageOfNums)

# Create a file data.txt with 3 lines of text
# Read the file
# Print each line separately
with open("data.txt", "w") as info: 
    info.write("This is first line. \nThis is second line. \nThis is third line.")

with open("data.txt", "r") as info: 
    readInfo = info.read()
    print(readInfo)

with open("data.txt", "r") as info: 
    for singleLineInfo in info: 
        print(singleLineInfo)

# Create a file numbers.txt
# Read numbers
# Convert to int
# Print total sum
with open("numbers.txt", "w") as data:
    data.write("10\n20\n30")

dataSum = 0

with open("numbers.txt", "r") as data: 
    for datum in data : 
        intDatum = int(datum)
        print(intDatum)
        dataSum = dataSum + intDatum
print(dataSum)
    
