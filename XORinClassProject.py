import numpy as np
characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]

def XOR(bit1,bit2):
    return "1" if bit1 != bit2 else "0"

def XORonByte(byte,key):
    byte = str(byte)
    key = str(key)
    decode = ""
    for i in range(len(byte)):
        decode += str(XOR(byte[i],key[i%len(key)]))
    return decode

#I don't need this function bc I made the key rolling, but still good to write down
def generateExactKey(message, key):
    new_key = ""
    if len(message) == len(key):
        new_key = key
    if len(message) > len(key):
        new_key += key * int(np.floor(len(message)/len(key)))
        new_key += key[0:(len(message)%len(key))]

    if len(message) < len(key):
        new_key = key[0:len(message)]
    return new_key

def XORonLetter(letter, keyLetter):

    letterBin = encode(letter)
    keyLetterBin = encode(keyLetter)

    encryptedLetter = XORonByte(letterBin,keyLetterBin)

    return decode(encryptedLetter)

print(XORonLetter("d","r"))

def XORonSentence(sentence,key):
    encryptedSentence = ""
    for i in range(len(sentence)):
        encryptedSentence += XORonLetter(sentence[i],key[i%len(key)])
    
    return encryptedSentence

print(XORonSentence("hello", "world"))
print(XORonSentence("rkAan","world"))

message = input("Input a message: ")
key = input("Enter a Key: ")

print("final answer ", XORonSentence(message,key))
