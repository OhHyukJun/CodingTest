import sys
from collections import deque

input = sys.stdin.readline
n = int(input()) # 부품의 총 개수
m = int(input()) # 부품간의 관계를 나타내는 간선의 수

indegree = [0] * (n+1) # 각 노드의 진입차수를 저장하는 리스트. 
graph = [[] for _ in range(n+1)] # 각 노드에 연결된 간선 정보를 저장하는 연결 리스트
cost = [[0] *(n+1) for _ in range(n+1)] # 각 부품을 만드는데 필요한 기본 부품의 수량을 저장하는 2차원 리스트

for _ in range(m):
    x,y,k = map(int,input().split())
    graph[y].append((x,k))
    indegree[x] += 1 
# 간선의 정보를 입력받은 뒤 그래프에 저장하고, 각 노드의 진입 차수를 계산하는 반복문
    
def topology_sort():
    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i) # 진입차수가 0인 노드를 큐에 추가
            cost[i][i] = 1 # 필요한 기본 부품의 수를 1로 설정
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            x,k = i[0],i[1]
            indegree[x] -= 1
            if indegree[x] == 0: 
                q.append(x) # 큐에서 노드를 하나씩 꺼내며 진입차수를 1씩 감소키기다가 진입 차수가 0이 된 노드는 다시 큐에 삽입하여 다음 순서를 진행한다.
            for j in range(1,n+1):
                cost[x][j] += cost[now][j] * k
            
topology_sort()
for i in range(1,n+1):
    if cost[n][i]:
        print(i,cost[n][i])