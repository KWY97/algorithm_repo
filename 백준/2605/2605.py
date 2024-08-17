students = int(input())
arr = list(map(int, input().split()))
line = []

# 첫번째 무조건 0번
# 두번째 0 or 1 -> 0뽑으면 그대로, 1뽑으면 앞에 놈 앞으로
# 세번째 0 or 1 or 2 -> 0뽑으면 그대로, 1뽑으면 앞에 높 앞으로, 2 뽑으면 앞에 놈 앞에 높 앞으로

for student, num in enumerate(arr): # student는 0 ~ (len(students) - 1), num은 뽑은 번호
    if num == 0:
        line.append(student)
    elif num




