# 첫 번째 풀이
T = int(input())

for _ in range(1, T+1):
    tc, n = input().split()
    words = input().split()

    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    result = ""
    for number in numbers:
        for word in words:
            if word == number:
                result += word + ' '

    print(tc)
    print(result)


# 두 번째 풀이 - 딕셔너리 활용 - 강의자료 보기
# 세 번쨰 풀이 - 카운팅 정렬 활용 - 강의자료 보기