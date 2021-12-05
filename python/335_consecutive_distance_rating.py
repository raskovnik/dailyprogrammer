def consec_distance(numbers):
    rating = 0
    l_numbers = list(enumerate(numbers))
    l_numbers.sort(key=lambda x:x[1])
    for i in range(0, len(l_numbers) - 1):
        if l_numbers[i + 1][1] - l_numbers[i][1] == 1:
            rating += l_numbers[i + 1][0] - l_numbers[i][0]
    return rating

print(consec_distance((1, 7, 2, 11, 8, 34, 3)))