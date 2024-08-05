T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N # 1번 부터 N번까지의 상자
    for i in range(1, Q+1): # i는 상자에 담길 값
        L, R = map(int, input().split()) # 시작과 끝 범위
        for j in range(L, R+1): # L부터 R까지
            arr[j-1] = i
    print(f'#{tc}', *arr)


T = int(input())
for tc in range(1, T + 1):
    n, q = map(int, input().split())
    a = [0] * n
    for i in range(1, q+1): # qq에 0과 1이 들어감
        i1, i2 = map(int, input().split())
        for j in range(i1 - 1, i2): # 인덱스 번호이기 때문에.
            a[j] = i
    print(f'#{tc}', *a