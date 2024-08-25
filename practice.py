def frog(arr, N, K):
    now = 1
    while now < N:
        if arr[now] == 1:
            now += K
            if now >= N:
                return N
        elif arr[now] == 0:
            for move in range(1, K):
                if arr[now - move] == 1:
                    now -= move
                    break
            else:
                return now
                

T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    ans = frog(arr, N, K)
    print(f'#{tc} {ans}')