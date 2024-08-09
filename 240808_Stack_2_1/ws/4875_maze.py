def find_maze(start_x, start_y): # 시작좌표
    visited = [[0] * N for _ in range(N)]
    stack = []

    x, y = start_x, start_y
    visited[start_x][start_y] = 1

    arr[x][y] = 0 # 시작점이니 나중에도 지나갈 수 있도록

    while True:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if arr[nx][ny] == 3:
                return 1

            if arr[nx][ny] != 0:
                continue

            if visited[nx][ny] != 0:
                continue

            stack.append([x, y])
            x, y = nx, ny
            visited[nx][ny] = 1
            break # for 문

        else: # 갈 곳이 없어 break 안걸린 경우
            if stack: # 스택에 남은게 있다면
                temp_li = stack.pop()
                x, y = temp_li[0], temp_li[1]
            else: # 스택에 남은게 없다면 탐색 종료
                return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 2:
                continue
            start_i = i
            start_j = j

    print(f'#{tc} {find_maze(start_i, start_j)}')