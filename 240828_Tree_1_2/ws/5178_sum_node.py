for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    h = [0 for _ in range(N+1)]

    for _ in range(M):
        leaf, value = map(int, input().split())
        h[leaf] = value

    while N > L*2-1:
        child = N
        parent = N//2
        h[parent] += h[child]
        N -= 1

    print(f'#{tc} {h[L]}')