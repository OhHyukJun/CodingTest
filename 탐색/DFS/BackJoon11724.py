'''
    깊이 우선 탐색(DFS) 
    그래프의 시작 노드에서 출발하여 탐색할 한 쪽 분기를 정하여 최대 깊이까지 탐색을 마친 후 다른 쪽 분기로 이동하여 다시 탐색을 수행하는 알고리즘
    깊이 우선 탐색은 실제 구현 시 재귀 함수를 이용하므로 스택 오버플로에 유의해야 함
    특징: 재귀함수로 구현, 스택 자료구조 사용 / 시간 복잡도(노드 수: V, 에지 수: E): O(V+E)
    단절점 착지, 단절선 찾기, 사이클 찾기, 위상 정렬등의 문제를 풀 때 사용
    
    1. DFS를 시작할 노드를 정한 후 사용할 자료구조 초기화
    2. 스택에서 노드를 꺼낸 후 꺼낸 노드의 인접 노드를 다시 스택에 삽입하기 
    3. 스택 자료구조에 값이 없을 때까지 반복 이때 한번 다녀간 노드는 방문 리스트를 바탕으로 재삽입하지 않는 것이 핵심
'''

#노드의 수 N 에지의 수 M 에지의 양 끝 u, v

import sys
sys.setrecursionlimit(10000)
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이므로 재귀함수를 사용할 때 필수적으로 선언해주어야함
input = sys.stdin.readline
n, m = map(int,input().split()) # 노드와 에지의 두 값을 입력받기 위해 map 함수를 사용
A = [[] for _ in range(n+1)] #그래프 데이터 저장 인접 리스트 초기화
visited = [False] * (n+1) #초기값이 false인 배열을 선언

def DFS(v): #dfs 선언
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
            
for _ in range(m):
    s, e = map(int,input().split())
    A[s].append(e) #양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)
    
count = 0

for i in range(1,n+1):
    if not visited[i]:
        count+=1
        DFS(i)
        
print(count)