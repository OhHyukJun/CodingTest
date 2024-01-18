from collections import deque

Max = 10 ** 5
N,K = map(int,input().split())
visited = [0] * (Max + 1)

def bfs():
    queue = deque([(N,0)])
    visited[N] = 1
    count = 0
    min_time = None

    while queue:
        X, time = queue.popleft()

        if min_time != None and time > min_time:
            continue

        if X == K:
            if min_time == None:
                min_time = time
            count += 1

        for i in (X-1, X+1, 2*X):
            if 0 <= i <= Max:
                if not visited[i] or (visited[i] and time + 1 <= visited[i]):
                    visited[i] = time + 1
                    queue.append((i, time+1))
    
    print(min_time)
    print(count)

bfs()