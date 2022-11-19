# taking 'string' input from the user
word = input("Enter a word that you wanto to encrypt: \n")
key = 2

# iterate through the string
word_encrypted = "";
for letter in word:
    # transform each character in ASCII shift it and retransform it in char
    word_encrypted += chr(ord(letter) + key)

print(word_encrypted)