def advanced_slice():
    
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