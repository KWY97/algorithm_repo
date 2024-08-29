def cal(left, right, operator):
    if operator == '+':
        ans = left + right
    elif operator == '-':
        ans = left - right
    elif operator == '*':
        ans = left * right
    else:
        ans = left / right
    return int(ans)

def postorder(n):
    if type(arr[n][1]) == type(''):
        left = postorder(arr[n][2])
        right = postorder(arr[n][3])
        return cal(left, right, arr[n][1])
    else:
        return arr[n][1]

for tc in range(1, 11):
    N = int(input())
    arr = [0] + [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    print(f'#{tc} {postorder(1)}')