alphabet = "abcdefghijklmnopqrstuvwxyz"
c_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXWZ"
def ceasar_cipher(c, x):
    #Optional Bonus 1
    #handle non-letter characters
    if c not in alphabet and c not in c_alphabet:
        return c
    
    #handle capital letters 
    if c not in alphabet: #if character not in small lettered alphabet check in the capitalized alphabet
        if c_alphabet.index(c) + x > len(c_alphabet) or c_alphabet.index(c) + x == len(c_alphabet) :
            return c_alphabet[(c_alphabet.index(c) + x) % len(c_alphabet)]
        else:
            return c_alphabet[(c_alphabet.index(c) + x)]

    if alphabet.index(c) + x > len(alphabet) or alphabet.index(c) + x == len(alphabet) :
        return alphabet[(alphabet.index(c) + x) % len(alphabet)]
    else:
        return alphabet[(alphabet.index(c) + x)]

def ceasar(s, x):
    shifted = ""
    for c in s:
        shifted += ceasar_cipher(c,x)
    return shifted

print(ceasar("Daily!", 6))
def decipher(c, x):
    letter_freq = [3,-1,1,1,4,0,0,2,2,-5,-2,1,0,2,3,0,-6,2,2,3,1,-1,0,-5,0,-7]
    