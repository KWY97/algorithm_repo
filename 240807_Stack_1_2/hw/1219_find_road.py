# A: 0, B: 99로 고정






T = 10
for _ in range(T):
    tc, N = map(int, input().split()) # N: 간선의 개수
    edges = list(map(int, input().split())) # 간선들의 연결 번호
    start, end = 0, 99
    adjL = [[] for _ in range(100)] # 정점은 최대 100개. 1~98은 정점, 0: 출발점, 99: 도착점
    for i in range(N):
        v1, v2 = edges[i*2], edges[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    sort_adjL = [sorted(row) for row in adjL]