N = int(input())
divisor = []
prime_num = []
my_ans = []

for i in range(2, N):
    if N % i == 0:
        divisor.append(i)

for num in divisor:
    temp = []
    for j in range(1, num):
        if num % j == 0:
            temp.append(num)
    if len(temp) == 1:
        prime_num.append(num)

max_prime = max(prime_num)

while N >= max_prime:
    for i in prime_num:
        if N % i == 0:
            N //= i
            my_ans.append(i)
            break

for i in my_ans:
    print(i)

# 잔디 심기용 수정 입니다.
