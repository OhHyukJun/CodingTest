'''
너비 우선 탐색(BFS)
 시작 노드에서 출발해 시작 노드를 기준으로 가까운 노드를 먼저 방문하면서 탐색하는 알고리즘
 FIFO 탐색 -> 선입선출 , Queue 자료구조를 이용
 1. BFS를 시작할 노드를 정한 후 사용할 자료구조 초기화하기
 2. 큐에서 노드를 꺼낸 후 노드의 인접 노드를 다시 큐에 삽입
 3. 큐 자료구조에 값이 없을 때까지 반복
'''

from collections import deque #큐를 사용하여 문제를 해결할 것이기에 사용
N, M, Start = map(int,input().split())
A = [[] for _ in range(N+1)]

for _ in range(M): #A 인접 리스트에 그래프 데이터 저장
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)
    
for i in range(N+1):
    A[i].sort() #번호가 작은 노드부터 방문하기 위해 정렬하기
    
def DFS(v):
    print(v, end=' ') #현재 노드 출력하기
    visited[v] = True #visited 리스트에 현재 노드 방문 기록하기
    for i in A[v]:
        if not visited[i]:
            DFS(i)  #현재 노드와 연결 노드 중 방문하지 않은 노드로 DFS 실행
 
visited = [False] * (N+1)
DFS(Start) #DFS 실행

def BFS(v):
    queue = deque()
    queue.append(v) #큐 자료구조에 시작 노드 삽입
    visited[v] = True
    while queue:
        now_Node = queue.popleft() #큐에서 노드 데이터 가져오기
        print(now_Node,end=' ') #현재 노드 출력하기
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i) #현재 노드와 연결 노드 중 미 방문 노드를 큐에 삽입하고 방문 리스트에 기록

print()
visited = [False] * (N+1)
BFS(Start)