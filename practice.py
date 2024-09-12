N = int(input())
max_num = 1
cnt = 1

while N > max_num:
    max_num = max_num + (6 * cnt)
    cnt += 1
print(cnt)