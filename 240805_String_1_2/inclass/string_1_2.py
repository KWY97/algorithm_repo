# 1. 고지식한 패턴 검색 알고리즘

# p = 찾을 패턴
# M = len(p)
# t = 전체 텍스트
# N = len(t)

# for문을 사용한 예시
p = 'TTA'
M = len(p) # 3
t = 'TTTTTABC'
N = len(t) # 8
cnt = 0

for i in range(N-M+1): # 비교 시작 위치
    for j in range(M): # 0 1 2
        if t[i + j] != p[j]:
            break # for j문을 break, 다음 글자부터 비교 시작
    else: # break 걸리지 않고 for j 문이 중단없이 반복되면
        cnt += 1 # 패턴 개수 1증가
print(cnt)


# 패턴과 일치하는 구간이 있으면 구간의 시작 인덱스 리턴, 없으면 -1 리턴하는 함수
def BruteForce_1(p, t):
    N = len(t)
    M = len(p)

    for i in range(N - M + 1):  # 비교 시작 위치
        for j in range(M):
            if t[i + j] != p[j]:
                break  # for j문을 break, 다음 글자부터 비교 시작
        else:  # break 걸리지 않고 for j 문이 중단없이 반복되면
            return i  # 패턴을 찾은 경우
    return -1 # 패턴을 못 찾은 경우



