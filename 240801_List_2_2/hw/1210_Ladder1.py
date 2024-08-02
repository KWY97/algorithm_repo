def search_ladder(x,y): # x: 시작하는 행, y: 시작하는 열
    arr[x][y] = 0 # 처음 시작하는 곳은 지났으니 0으로

    while x != 0: # 이 안에 무엇인가 자리가 잘못된듯 (들여쓰기 같은 것)
        for dx, dy in dxy:
            # nx, ny는 이동하려는 좌표
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or ny >= block_size: # 위로만 가기 때문에 nx >= block_size 안해도댐
                continue
            if not arr[nx][ny]:
                continue

            x, y = nx, ny
    return y

for _ in range(1, 11):
    tc = int(input())
    result = -1 # 찾지 못할 시 -1
    block_size = 100
    arr = [list(map(int, input().split())) for _ in range(block_size)]
    dxy = [[-1, 0], [0, -1], [0, 1]]

    for j in range(block_size):
        if arr[block_size-1][j] == 2:
            result = search_ladder(block_size-1, j)
            break

    print(f'#{tc} {result}')


