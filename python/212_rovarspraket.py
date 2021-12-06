def encode(sentence):
    vowels = "aeiou"
    s = "".join(i if i.lower() in vowels else i + "o" for i in sentence)
    return s

print(encode("Jag talar Rövarspråket!"))