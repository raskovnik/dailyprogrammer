def partition(arr):
    for i in range(0, len(arr) ):
        for j in range(1, len(arr)):
            if arr[i] % 2 == 0 and arr[j] % 2 != 0:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(partition([1,2,3,3,5,6,7,7,8,9]))