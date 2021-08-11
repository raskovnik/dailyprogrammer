from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def int_comp(n):
    ssum = []
    for i in factors(n):
        for j in factors(n):
            if i != 1 and j != 1 and i * j == n:
                ssum.append(i + j)
    return min(ssum)
print(int_comp(12345))