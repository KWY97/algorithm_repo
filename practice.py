# 버블 정렬 - 시간 복잡도: O(n**2)
arr = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
N = len(arr)

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# 카운팅 정렬 - 시간 복잡도: O(n+k), n은 리스트 길이, k는 정수의 최댓값
arr = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(arr)
M = max(arr)

counts = [0] * (M+1)
temp = [0] * N

for x in arr:
    counts[x] += 1

for i in range(1, len(counts)):
    counts[i] += counts[i-1]

for j in range(N-1, -1, -1):
    counts[arr[j]] -= 1
    temp[counts[arr[j]]] = arr[j]

print(temp)
