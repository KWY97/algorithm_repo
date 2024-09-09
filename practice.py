def my_dfs(n):
    # 종료 조건
    global cal

    if n == N - 1:
        ans.append(cal)
        return

    for i in range(4):
        if opers[i] == 0:  # 연산할 수 없는 경우 다음 연산자로 넘김
            continue
        cal2 = cal
        opers[i] -= 1

        if i == 0:
            cal += nums[n + 1]
        elif i == 1:
            cal -= nums[n + 1]
        elif i == 2:
            cal *= nums[n + 1]
        else:
            cal = int(cal / nums[n + 1])
        my_dfs(n + 1)
        opers[i] += 1
        cal = cal2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cal = nums[0]  # 처음 값 넣고 시작
    ans = []
    my_dfs(0)
    print(ans)
    print(f'#{tc} {max(ans) - min(ans)}')
