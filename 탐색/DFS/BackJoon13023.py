import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N,M = map(int,input().split())
arrive = False
A = [[] for _ in range(N+1)]
visited = [False]*(N+1)

def DFS(now, depth):
    global arrive
    if depth == 5: #깊이가 5가되면 출력
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i , depth+1) #재귀 호출마다 1씩 증가
    visited[now] = False
    
for _ in range(M):
    a, b = map(int,input().split()) 
    A[a].append(b)
    A[b].append(a) #양방향 애자아므로 값을 양쪽으로 증가

for i in range(N):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)

else:
    print(0)