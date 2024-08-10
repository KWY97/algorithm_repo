def f(i, N, v):
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f(i+1, N, v)
    


arr = [1, 2, 3, 4, 5]
N = len(arr)

print(f(0, N, 3))

