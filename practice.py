A, B = input().split()

if int(A[::-1]) > int(B[::-1]):
    max_v = A[::-1]
else:
    max_v = B[::-1]

print(max_v)