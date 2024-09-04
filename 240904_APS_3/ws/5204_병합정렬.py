def merge_sort(div_arr):
    global result

    if len(div_arr) <= 1:
        return div_arr

    mid = len(div_arr) // 2
    left = merge_sort(div_arr[:mid])
    right = merge_sort(div_arr[mid:])

    left_idx, right_idx, k = 0, 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            div_arr[k] = left[left_idx]
            left_idx += 1
        else:
            div_arr[k] = right[right_idx]
            right_idx += 1
        k += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))