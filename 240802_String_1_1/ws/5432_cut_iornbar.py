laser = {}
bar = {}
stack = []

T = int(input())

for tc in range(1, T+1):
    bracket = list(input())
    N = len(bracket)
    skip = 0 # 레이저와 일치하는 패턴을 찾았을 때, 해당 패턴의 길이만큼 인덱스를 건너 뛰기 위해 사용
    cnt = 1

    for i in range(N-1): # 레이저와 쇠막대기 위치파악, i와 i+1과 비교를 하기위해 범위는 N-1
        if i != N-2:       
            if skip > 0:
                skip -= 1
                continue # for i문으로 이동 
            if bracket[i] == '(' and bracket[i+1] == ')': # 레이저 위치 확인
                laser['laser' + str(cnt)] = [i, i+1]
                cnt += 1
                skip = 1
            else: # (( or )( or ))
                stack.append(i)
        else: # i가 N-2일 때
            if bracket[i] == '(' and bracket[i+1] == ')':
                laser['laser' + str(cnt)] = [i, i+1]
            else: # ), )
                stack.append(i)
                stack.append(i+1)

    # laser 인덱스와 bar 인덱스 찾기 완료
    
    
