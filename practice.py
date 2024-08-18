def Omok(N):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0
                ni, nj = i, j

                while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    ni += dxy[k][0]
                    nj += dxy[k][1]
    return 'NO'

dxy = [[0, 1], [1, 1], [1, 0], [1, -1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {Omok(N)}')