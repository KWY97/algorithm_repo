import sys
from collections import deque

def my_bfs(s):
    global num
    queue.append(s)
    visited[s] = num
    num += 1

    while queue:
        n = queue.popleft()

        for next in adjL[n]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = num
                num += 1

N, M, R = map(int, sys.stdin.readline(). split())
adjL = [[] for _ in range(N + 1)]
queue = deque()
visited = [0] * (N + 1)
num = 1

for _ in range(M):
    u, v = map(int, input().split())
    adjL[u].append(v)
    adjL[v].append(u)

for i in range(N + 1):
    adjL[i].sort()

my_bfs(R)
for v in range(1, N+1):
    print(visited[v])