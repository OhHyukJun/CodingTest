'''시작->레버->탈출 시작과 레버를 찾고 탐색하기'''
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def find(maps):
    col = len(maps)
    row = len(maps[0])
    for i in range(col):
        for j in range(row):
            if maps[i][j] == 'S':
                start = (j,i)
            elif maps[i][j] == 'L':
                lever = (j,i)
    return start,lever

def bfs(start, target, maps):
    col = len(maps)
    row = len(maps[0])
    x,y = start
    visited = [[False]*row for _ in range(col)]
    visited[y][x] = True
    
    queue = deque([(x,y,0)])
    
    while queue:
        x,y,distance = queue.popleft()
        if maps[y][x] == target:
            return distance
        
        for i in range(4):
            dx1 = x + dx[i]
            dy1 = y + dy[i]
            if -1<dx1<row and -1<dy1<col and not visited[dy1][dx1] and maps[dy1][dx1] != 'X':
                visited[dy1][dx1] = True
                queue.append((dx1,dy1,distance+1))
    return -1

def solution(maps):
    answer = 0
    start,end = find(maps)
    lever_distance = bfs(start,'L',maps)
    if lever_distance < 0:
        return -1
    end_distance = bfs(end,'E',maps)
    if end_distance < 0:
        return -1
    else:
        return lever_distance+end_distance