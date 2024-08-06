def search_len(x, y, start):  # x, y, start의 좌표를 입력받음. - start는 초기 y값
    cnt = 0  # 경로를 셀 변수
    while x < N - 1:  # x는 0 ~ N-2행 까지만 실행, N-1행이 마지막 행이기 때문
        arr[x][y] = 0  # 자기 자리는 지나 갔으니 0으로 (좌, 우로 갈 때 되돌아가지 않기 위해서)
        print(x,y)
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx >= N or ny < 0 or ny >= N:  # 범위를 벗어난 경우 continue
                continue

            if arr[nx][ny] != 1:  # 1이 아닌 경우 continue
                continue

            x, y = nx, ny
            cnt += 1
            break

    return {start: cnt}


T = 10
dxy = [[0, 1], [0, -1], [1, 0]]  # 우, 좌, 하 순서로 탐색

for _ in range(T):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans_dic = {}  # key: 시작 열 인덱스, value: 해당 인덱스의 경로의 길이
    start_li = []  # 시작할 수 있는 지점을 담을 리스트

    for i in range(N):  # arr[0]의 모든 열에서 값이 1인 것을 찾음
        if arr[0][i] == 1:
            start_li.append(i)  # 시작 인덱스를 모으는 start_li에 추가
    for j in start_li:
        ans_dic.update(search_len(0, j, j))
        print(ans_dic)

    min_value = min(ans_dic.values())  # 최소 경로 값 뽑음
    key_list = [key for key in ans_dic if ans_dic[key] == min_value]  # 최소 경로의 키 들을 뽑고 리스트에 담음
    ans = (max(key_list))  # 최소 경로를 가지는 인덱스 키 중 가장 큰 값

    print(f'#{tc} {ans}')