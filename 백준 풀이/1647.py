'''
모든 길에 대한 정보를 입력받습니다.
저장된 길의 정보를 비용이 낮은 순으로 정렬
비용이 낮은 순서대로 길을 확인하면서 두 집이 아직 연결되지 않았다면 연결하고, 비용을 합산합니다.
마지막에 연결된 길의 비용을 빼주면 길을 없애고 남은 유지비의 최소값을 구할 수 있습니다.
'''
import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
        
N,M = map(int,input().split())
parent = [0] * (N+1)

edges = []
result = 0

for i in range(1, N+1):
    parent[i] = i
    
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
    
edges.sort()

large = 0 # 제일 비용이 큰 간선

for edge in edges:
    c,a,b = edge
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result += c
        large = c
        
print(result - large)