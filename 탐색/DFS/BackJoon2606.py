N = int(input()) #컴퓨터의 수
M = int(input()) #연결된 수
graph = [[]*N for _ in range(N+1)] #쌍을 입력받을 그래프

for _ in range(M):
    s, e = map(int,input().split()) #두 수 입력
    graph[s].append(e)
    graph[e].append(s)
    
count = 0
visited = [0] * (N+1)

def DFS(start): #탐색 함수 정의
    global count
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            DFS(i)
            count += 1

DFS(1)
print(count)