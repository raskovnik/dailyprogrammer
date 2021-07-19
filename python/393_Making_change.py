#exercise number 393 from r/dailyprogrammer
from math import floor
units = [500, 100, 25, 10, 5, 1]
def make_change(x):
    count = 0
    for i in range(len(units)):
        if x < units[i] :
            pass
        else:
            count += floor(x / units[i])
            x = x % units[i]

    return count
print(make_change(468))