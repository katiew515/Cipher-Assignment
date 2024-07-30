# add your code here
#for every letter in the string entered by the user
#iterate through the string and for each character 
#add 5 alphabetically (create a key/dictonary?)
#print that response back out 
def cipher(user_string):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    ciphered_string = ""
    for character in user_string:
        if character.isalpha():
            original_index=alphabet.index(character)
            new_index= (original_index + 5) % 26
            ciphered_string+= alphabet[new_index] 
        else:
            ciphered_string += character
    return ciphered_string
user_string= input("Enter your message (lowercase only):")
print(cipher(user_string))