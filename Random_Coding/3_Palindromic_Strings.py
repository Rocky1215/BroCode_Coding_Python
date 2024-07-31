def maincode():
    userstring = input("Enter a palindrome. A palindrome is a word or "+ \
                       "number that can be read the same both ways: ")
    userstring = userstring.lower()
    reversestring = ''.join(reversed(userstring))
    if userstring == "":
        print("Try typing in something next time.")
    elif reversestring == userstring:
        print("Yay, you entered a palindrome!")  
    else:
        print("No palindrome! Try again!")
maincode()