from collections import deque

def bfs(x,y,color):
    count = 0
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0
    while queue:
        x1,y1 = queue.popleft()
        count += 1
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == color:
                arr[nx][ny] = 0
                queue.append((nx,ny))
    return count
        

n,m = map(int,input().split())
arr = [list(input()) for _ in range(m)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
white = 0
blue = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 'W':
            #print(bfs(i,j,'W'))
            white += bfs(i,j,'W')**2
        elif arr[i][j] == 'B':
            blue += bfs(i,j,'B')**2
            
print(white,blue)