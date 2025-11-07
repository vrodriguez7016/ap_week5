def length_count():

    # Length and Count:
    # a. Calculate the number of characters (including spaces and punctuation) in the word/
    phrase ="Supercalifragilisticexpialidocious"
    print(len(phrase))
    # b. Count the number of times the letter 'i' appears in the same word/phrase.
    letter = "i"
    counter = phrase.count(letter)
    print(f"The character {letter} appears {counter} times in the phrase: {phrase}.")
