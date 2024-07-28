from collections import deque

n,m = map(int,input().split())
arr = [[0]*m for _ in range(n)]

for i in arr:
    numbers = list(input())
    for j in range(m):
        i[j] = int(numbers[j])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

queue = deque()
queue.append((0,0))

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0  and arr[nx][ny] == 1:
            #print(nx,ny)
            queue.append((nx,ny))
            visited[nx][ny] = 1
            arr[nx][ny] = arr[x][y] + 1
            
print(arr[-1][-1])