T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_value = arr[0]
    max_value = arr[0]

    for i in range(1, N):
        if min_value > arr[i]:
            min_value = arr[i]
    min_index = arr.index(min_value)
    min_ans = min_index + 1

    for j in range(1, N):
        if max_value < arr[j]:
            max_value = arr[j]
    reverse_arr = arr[::-1]
    max_reverse_index = reverse_arr.index(max_value)
    max_ans = (N-1-max_reverse_index) + 1

    print(f'#{tc} {abs(max_ans - min_ans)}')