from collections import deque

n,m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
visited = [[0]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
    
queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            queue.append((i,j))
            visited[i][j] == 1
            arr[i][j] = 0
            break
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] != 0:
            arr[nx][ny] = arr[x][y] + 1
            visited[nx][ny] = 1
            queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and visited[i][j] == 0:
            arr[i][j] = -1
        print(arr[i][j],end=' ')
    print('')
#print(arr)
