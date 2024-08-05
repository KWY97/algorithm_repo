def search_len(x, y): # x, y의 좌표를 입력받음.

T = 10
N = 100
dxy = [[0, 1], [0, -1], [1, 0]] # 우, 좌, 하 순서로 탐색

for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        if arr[0][i] == 1:
            # search_len(0, i)
            pass
