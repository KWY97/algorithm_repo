# 강사님 sol 보고 푼 것
def f(i, j, bw, N):
    board[i][j] = bw
    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i + di, j + dj
        tmp = []

        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            tmp.append((ni, nj))
            ni += di
            nj += dj

        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw: # while문 나왔을 때 범위안에 들어 있고, 반대 돌이라서 빠져 나온 것이라면
            for p, q in tmp:
                board[p][q] = bw

B = 1
W = 2
op = [0, 2, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    play = [list(map(int, input().split())) for _ in range(M)]

    # 보드 생성
    board = [[0] * N for _ in range(N)]

    # 중심 돌 배치
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W

    for col, row, bw in play:
        f(row-1, col-1, bw, N)

    B_cnt = W_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                B_cnt += 1
            elif board[i][j] == W:
                W_cnt += 1

    print(f'#{tc} {B_cnt} {W_cnt}')