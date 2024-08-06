def pascal(N):
    '''
    줄의 개수는 N줄
    끝과 끝은 1
    i번째 줄의 원소는 i개
    '''
    for i in range(1, N+1): # 줄
        for j in range(1, i+1): # 원소의 개수만큼 반복









T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 파스칼 삼각형의 크기
    arr = [[0] * N for _ in range(N)]

    # ans = pascal(N)
    # print(f'#{tc}')
    # print(ans)