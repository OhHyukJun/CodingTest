'''
    4*6 배열로 표현되는 1과 0으로 이루어진 미로에서 (1,1)에서 출발해 (N,M)의 위치로 이동하기 위해 지나야하는 칸 수의 최솟값을 구하는 프로그램
    1번 째 줄에 N,M을 입력받고 그 이후 N개의 줄에는 미로의 내용이 M개의 정수로 주어짐
'''

from collections import deque

dx = [0,1,0,-1] #좌우 탐색
dy = [1,0,-1,0] #상하 탐색 

N,M = map(int,input().split()) #가로 = N 세로 = M
A = [[0] * M for _ in range(N)] #M개의 배열이 N번 반복되는 행렬 A
visited = [[False] * M for _ in range(N)] #방문 기록 저장 리스트

for i in range(N): 
    numbers = list(input()) #numbers 변수를 리스트로 입력받음
    for j in range(M):
        A[i][j] = int(numbers[j]) #A 리스트에 데이터 저장
        
def BFS(i,j):
    queue = deque() #큐에 시작 노드를 삽입
    queue.append((i,j)) 
    visited[i][j] = True #visited 리스트에 현재 노드 방문 기록
    
    while queue: # 큐가 비어 있을 때까지 반복
        now = queue.popleft() #큐에서 노드 데이터를 가져오기
        for k in range(4): # 상 하 좌 우 4번 탐색
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < N and y < M: #좌표 유효성 검사
                if A[x][y] != 0 and not visited[x][y]: #이동할 수 있는 칸이면서 방문하지 않은 노드이면
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] + 1 #A 리스트에 depth를 현재 노드의 depth+1로 업데이트
                    queue.append((x,y)) #큐에 데이터를 삽입
                
BFS(0,0)
print(A[N-1][M-1])
    