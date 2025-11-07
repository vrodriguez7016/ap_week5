def problem4():

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