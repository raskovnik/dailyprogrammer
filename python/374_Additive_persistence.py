def persistence(number):
    sums = 0
    while number > 9:
        number = sum_digits(number)
        sums += 1
    return sums

def sum_digits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

print(persistence(1234))