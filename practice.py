chess, my_chess = [1, 1, 2, 2, 2, 8], list(map(int, input().split()))

for i in range(len(my_chess)):
    if my_chess[i] == chess[i]: chess[i] = 0
    else: chess[i] = chess[i] - my_chess[i]
print(*chess)