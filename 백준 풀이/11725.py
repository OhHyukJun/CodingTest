import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(N-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(v):
    for i in arr[v]:
        if visited[i] == -1:
            visited[i] = v
            dfs(i)
        
dfs(1)
for i in range(2,N+1):
    print(visited[i])