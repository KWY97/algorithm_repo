def find_start():
    for i in range(size):
        for j in range(size):
            if arr[i][j] == '2':
                return i, j

def search_road(st_x, st_y):
    visited = [[0] * (size) for _ in range(size)]
    stack = []

    x, y = st_x, st_y
    visited[x][y] = 1

    while True:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= size or ny >= size or visited[nx][ny] == 1 or arr[nx][ny] == 1:
                continue
            if arr[nx][ny] == 3:
                return 1








size = 16
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(1, 11):
    tc = int(input())
    arr = [[input()] for _ in range(size)]
    start_x, start_y = find_start()
    search_road(start_x, start_y)



