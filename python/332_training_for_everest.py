from random import randint

def everest(n):
    peaks = [n.split()[randint(0, len(n.split()))]]
    curr_index = 0
    for i in n.split():
        if int(i) > int(peaks[curr_index]):
            peaks.append(i)
            curr_index += 1

    return peaks

print(everest("0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15"))
print(everest("1 2 20 13 6 15 16 0 7 9 4 0 4 6 7 8 10 18 14 10 17 15 19 0 4 2 12 6 10 5 12 2 1 7 12 12 10 8 9 2 20 19 20 17 5 19 0 11 5 20"))
