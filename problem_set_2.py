def problem2():
    
    # Problem Set 2: Extracting Information  vr
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    print(quote.find('John F. Kennedy'))  #find certain phrases in string
    personality_name = quote [78:] # cleaner
    print(personality_name) # John F. Kennedy    