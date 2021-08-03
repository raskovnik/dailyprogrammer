def upc_digit(code):
    d_s, x_s = 0, 0
    for d in code[::2]: # sum of digits at even indexes
        d_s += int(d)
    for x in code[::1]: # sum of digits at odd indexes
        x_s += int(x)
    if (d_s * 3 + (x_s - d_s)) % 10 != 0:
        return 10 - ((d_s * 3 + (x_s - d_s)) % 10)
    else:
        return 0
print(upc_digit("03600029145"))