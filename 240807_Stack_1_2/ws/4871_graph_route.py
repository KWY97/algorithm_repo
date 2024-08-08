def my_dfs(s, V):
    visited = [0] * (V+1)
    stack = []
    sp = s
    visited[sp] == 1

    while True:
        for np in adjL[sp]:
            if visited[np] == 0:
                stack.append(sp)
                sp = np
                visited[np] == 1
                break # for np문에 걸림
        else:
            if stack:
                sp = stack.pop()
            else:  
                break # while문에 걸림
        if sp == end:
            return 1
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    edge = [] # 간선들의 번호를 담을 리스트
    for _ in range(E):
        temp1, temp2 = map(int, input().split())
        edge.append(temp1)
        edge.append(temp2)
    
    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = edge[i*2], edge[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    start, end = map(int, input().split()) # 출발 정점, 도착 정점

    print(f'#{tc} {my_dfs(start, V)}')