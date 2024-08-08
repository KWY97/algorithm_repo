# A: 0, B: 99로 고정

def my_dfs(V, s = 0): # s: 시작정점, V: 정점의 개수
    visited = [0] * 100
    visited[s] = 1





T = 10
for _ in range(T):
    tc, E = map(int, input().split()) # E: 간선의 개수
    arr = list(map(int, input().split())) # 간선들의 연결 번호
    adjL = [[] for _ in range(100)] # 정점은 최대 100개. 1~98은 정점, 0: 출발점, 99: 도착점
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    sort_adjL = [sorted(row) for row in adjL]