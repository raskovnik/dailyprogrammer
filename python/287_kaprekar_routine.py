def largest_digit(number): return int("".join(sorted(str(number)))[len(str(number)) - 1])

def descending_digits(number): return int("".join(sorted(str(number)))[::-1])

print(descending_digits(1548))