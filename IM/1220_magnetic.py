T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 전치행렬로 바꾸기
    for temp_1 in range(N):
        for temp_2 in range(N):
            if temp_1 > temp_2:
                arr[temp_1][temp_2], arr[temp_2][temp_1] = arr[temp_2][temp_1], arr[temp_1][temp_2]

    for i in range(N):
        for j in range(N):
            for k in range(1, N-j):
                if arr[i][j] == 1:
                    if arr[i][j+k] == 2:
                        cnt += 1
                        break  # for k 문
                        # 2를 발견한 위치의 바로 뒤부터 반복문이 다시 실행되어 1을 찾게해야함
                        # while로 범위 내에서만 실행하게 조건도 걸어야 할 듯



