from collections import deque #bfs 구현 시 사용할 라이브러리

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a) #1,2일 때 양방향으로 저장

for i in range(N+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft() #큐의 시작값
        print(v,end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (N+1)
dfs(graph,V,visited)
print("")

visited = [False] * (N+1)
bfs(graph,V,visited)

