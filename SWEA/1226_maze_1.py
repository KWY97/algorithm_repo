def my_dfs(sx, sy):
    visited[sx][sy] = 1

    # 현재 위치가 도착점이면 1을 반환
    if arr[sx][sy] == '3':
        return 1

    # 네 방향으로 탐색
    for dx, dy in dxy:
        nx = sx + dx
        ny = sy + dy

        # 다음 위치가 유효하고, 아직 방문하지 않았으며, 벽이 아니면
        if 0 <= nx < size and 0 <= ny < size and arr[nx][ny] != '1' and visited[nx][ny] == 0:
            if my_dfs(nx, ny) == 1:
                return 1  # 도착점을 찾으면 1을 반환

    return 0  # 모든 방향을 다 탐색해도 도착점을 찾지 못하면 0 반환

def find_start(arr, size):
    for i in range(size):
        for j in range(size):
            if arr[i][j] == '2':
                return i, j

size = 16
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[0] * size for _ in range(size)]

for _ in range(1):
    tc = int(input())
    arr = [list(input()) for _ in range(size)]
    start_x, start_y = find_start(arr, size)
    print(f'#{tc} {my_dfs(start_x, start_y)}')