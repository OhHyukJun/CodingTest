from collections import deque

n = int(input())
arr = [[0]*n for _ in range(n)]
for i in arr:
    numbers = list(input())
    for j in range(n):
        i[j] = int(numbers[j])

answer = []

def bfs(x,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1

    queue = deque()
    queue.append((x,y))
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                arr[nx][ny] = 0
                count += 1
    answer.append(count)
    
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i,j)
            

answer.sort()
print(len(answer))
for i in answer:
    print(i)            