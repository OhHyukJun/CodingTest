
from collections import deque

Max = 10 ** 5
N, K = map(int,input().split())
visited = [0] * (Max+1)

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        X = queue.popleft()
        if X == K:
            print(visited[X])
            break
        for i in (X-1,X+1,2*X):
            if 0 <= i <= Max:
                if not visited[i]:
                    visited[i] = visited[X] + 1
                    queue.append(i)

bfs()

