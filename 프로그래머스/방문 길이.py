def solution(dirs):
    answer = 0
    visited = set()
    x,y = 0,0
    dir = {'L':(-1,0), 'R':(1,0), 'U':(0,1), 'D':(0,-1)}
    for i in range(len(dirs)):
        dx,dy = dir[dirs[i]]
        nx = x + dx
        ny = y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited:
                visited.add((x,y,nx,ny))
                answer += 1
            x,y = nx,ny
    return answer