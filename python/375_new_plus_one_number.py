def plus_one(number):
    new = ""
    for n in str(number): new += str(int(n) + 1)
    return new

print(plus_one(998))