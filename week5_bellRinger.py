# Problem Set 1: Indexing and Slicing Strings ac
# Basic Indexing:
# Given the string 
magic = 'abracadabra'
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.

print(magic[4])
print(magic[-2])
print(magic[5])

# Advanced Slicing:
# Given the string 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
print(alphabet[7:10]) # extract the letters 'hij'
second_letters = alphabet[0:13:2] # extract every second letter from 'a' to 'm'
print(second_letters)
reverse = alphabet[::-1] # reverse the entire string using slicing
print(reverse)

# Problem Set 2: Extracting Information  vr
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find('John F. Kennedy'))  #find certain phrases in string
personality_name = quote [78:] # cleaner
print(personality_name) # John F. Kennedy

# Manipulating Words: ac
# Given the string 
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
word1 = "subjective"

if word1 in info:
    print(f"{word1}")
else:
    print("Not found.")

info1 = info.split('Python is fun. Fun is good. Good is subjective.')
third_words = info1[:2] # this joins them back into a string 
print(third_words)

reverse1 = info1[::-1] # this reverses the orders of words 

# Problem Set 3: String Methods vr
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
phrase = "May the force be with you."
print("Lowercase:", phrase.lower())
print("Uppercase:", phrase.upper())

# String Joining and Splitting: vr
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
mottos = ["Make", "haste", "slowly."]
separator = " "
result_string = separator.join(mottos)
print(result_string)

# Replacing Words: vr
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
original_string = "Life is what happens when you are busy making other plans."
new_string = original_string.replace ("busy", "distracted")
print(new_string)

new_string1 = original_string.replace ("plans", "mistakes")
print(new_string1)

# Problem Set 4: String Properties and Advanced Operations ac
# Repetition:
# Concatenate the word "Iteration" 7 times.
word = "Iteration"
print(word*7)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word = "moonlight"
if word in quote:
    print("Moonlight found in quote.")
else:
    print("Moonlight not found in quote.")

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/
phrase ="Supercalifragilisticexpialidocious"
print(len(phrase))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
letter = "i"
counter = phrase.count(letter)
print(f"The character {letter} appears {counter} times in the phrase: {phrase}.")
