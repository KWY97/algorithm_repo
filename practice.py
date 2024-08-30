def make_tree(n):
    global num
    if n <= N:
        make_tree(2*n)
        tree[n] = num
        num += 1
        make_tree(2*n+1)
    return tree

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = 1
    tree = [0] * (N+1)
    ans = make_tree(1)
    print(f'#{tc} {ans[1]} {ans[N//2]}')