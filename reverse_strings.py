def reverse():

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
