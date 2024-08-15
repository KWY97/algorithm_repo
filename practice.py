T = 2

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    print(arr)