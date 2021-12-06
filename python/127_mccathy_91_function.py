def mccathy91(n):
    return n-10 if n > 100 else mccathy91(mccathy91(n + 11))

print(mccathy91(0))