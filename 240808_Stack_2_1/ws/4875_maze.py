# 0: 통로, 1: 벽, 2: 출발, 3: 도착

def maze(x, y): # 시작 좌표
    # x, y = 찾아야함
    ans = 0

    while True: # 조건 생각해봐야함
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if arr[nx][ny] != 0: # 통로가 아니라면
                continue

            x, y = nx, ny

            if arr[x][y] == 3:
                ans = 1
                break # while 문
    return ans




    



T = int(input())
dxy = [[0, 1], [1, 0], [-1, 0], [0, 1]]

for tc in range(1, T+1):
    N = int(input()) # 미로의 크기: N * N
    arr = [list(map(int, input())) for _ in range(N)]
    
    # 시작점 찾기 -> 필요
    
        
    