from collections import deque

N = int(input()) #노드의 개수
A = [[] for _ in range(N+1)] #그래프 데이터 저장 인접 리스트

for _ in range(N):
    Data = list(map(int,input().split())) #입력받을 앞의 두 수
    index=0 
    S = Data[index]  
    index += 1
    while True:
        E = Data[index] # 두 수간의 깊이 E
        if E == -1: #-1이면 종료
            break
        V = Data[index + 1] # 다음 경로 V
        A[S].append((E,V)) 
        index+=2
        
distance = [0] * (N+1)
visited = [False] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v) #큐 자료구조에 시작 노드 삽입
    visited[v] = True #visited 리스트에 현재 노드 방문 기록
    while queue: #큐가 비어있을 때까지
        now_Node = queue.popleft() #큐에서 노드 데이터를 가져오기
        for i in A[now_Node]: #현재 노드의 연결노드일 때까지 반복
            if not visited[i[0]]: #미방문 노드이면
                visited[i[0]] = True
                queue.append(i[0]) #큐에 데이터 삽입
                distance[i[0]] = distance[now_Node] + i[1] #거리 리스트 업데이트
                
BFS(1) #임의의 점을 시작점으로 실행
Max = 1 #distance 리스트에서 가장 큰 값을 지닌 노드를 시작점으로 지정

for i in range(2, N+1):
    if distance[Max] < distance[i]:
        Max = i #거리 리스트값 중 Max값으로 시작점 재설정
        
distance = [0] * (N+1)
visited = [False] * (N+1)
BFS(Max)
distance.sort() 
print(distance[N]) #distance 리스트에서 가장