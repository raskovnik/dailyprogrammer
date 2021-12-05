def camel_case(words):
    s = "".join(word[0].upper() + word[1:].lower() for word in words[1:])
    return s[0].lower() + s[1:]

def snake_case(words):
    s = "".join(word + "_" for word in words[1:])
    return s[:len(s) - 1]

words = input("Enter a number followed by sentence to convert separated by spaces: ").split()
if int(words[0]) == 0:
    print(camel_case(words))

if int(words[0]) == 1:
    print(snake_case(words))

if int(words[0]) == 2:
    print(snake_case(words).upper())