T = int(input())

# 전치행렬 사용해야 할 듯
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans_list = []

    # 행 기준 탐색
    for i in range(N): # 모든 행에 대해
        for j in range(N-M+1): # 윈도우의 시작 인덱스
            for k in range(M//2): # 회문 검사를 위한 횟수
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break # for k문 탈출, 윈도우 재탐색
            else:
                for l in range(M):
                    ans_list.append(arr[i][j+l])
    ans = "".join(ans_list)

    # 열 기준 탐색
    # 전치행렬 만들어 주기
    for i in range(N):
        for j in range(N):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
    # 이후 과정은 동일
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else:
                for l in range(M):
                    ans_list.append(arr[i][j+l])
    ans = "".join(ans_list)

    print(f'#{tc} {ans}')