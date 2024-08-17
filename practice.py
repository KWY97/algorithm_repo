def left_shift(arr, n):
    new_arr = [None for _ in range(len(arr))]
    for i in range(len(arr)):
        new_arr[i-n] = arr[i]
    return new_arr

def right_shifr(arr, n):
    new_arr = [None for _ in range(arr)]
    for i in range(len(arr)):
        new_arr[i] = arr[i-n]
    return new_arr

arr = [1, 2, 3, 4, 5]

ans = left_shift(arr, 1)
print(ans)