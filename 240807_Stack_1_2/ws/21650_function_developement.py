def solution(progresses, speeds):
    day_list = []  # 각 작업별 남은 일수를 저장할 리스트. 작업 순서대로 인덱스 순서도 결정됨.
    ans_list = []  # 답을 담을 list
    N = len(progresses)

    for i in range(N):
        if (100 - progresses[i]) % speeds[i] == 0:  # 나눠지는 경우
            day_list.append(int((100 - progresses[i]) / speeds[i]))
        else:  # 나눠지지 않는 경우
            day_list.append(int((100 - progresses[i]) // speeds[i] + 1))  # 몫 + 1은 일수가 됨

    cnt = 1

    for i in range(N - 1): # len(day_list) == len(progresses)이므로 N사용. 뒷 글자와 비교할 것이기 때문에 범위는 N-1까지
        if day_list[i] >= day_list[i + 1]:
            cnt += 1
        else:
            ans_list.append(cnt)
            cnt = 1

    ans_list.append(cnt)

    answer = ans_list
    return answer

progresses = [90, 90, 90]
speeds = [1, 5, 4]

print(solution(progresses, speeds))