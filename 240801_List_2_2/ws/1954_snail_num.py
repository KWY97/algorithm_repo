T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    for x in range(N):
        for y in range(N):
            if N == 1:
                ans = 1
                break
            else:
                