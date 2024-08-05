# 1. 고지식한 패턴 검색 알고리즘

# while문을 사용한 식
# p = 찾을 패턴
# M = len(p)
# t = 전체 텍스트
# N = len(t)

while i < N and j < M:
    if t[i] == p[j]: # 일치하는 경우
        i += 1
        j += 1
    else: # 불일치하는 경우
        i = i - j + 1
        j = 0

# for문을 사용한 예시 문제
p = 'TTA'
M = len(p)
t = 'TTTTTABC'
N = len(t)
cnt = 0

for i in range(N-M+1): # 비교 시작 위치
    for j in range(M):
        if t[i + j] != p[j]:
            break # for j문을 break, 다음 글자부터 비교 시작
    else: # break 걸리지 않고 for j 문이 중단없이 반복되면
        cnt += 1 # 패턴 개수 1증가
print(cnt)














# 2. KMP 알고리즘