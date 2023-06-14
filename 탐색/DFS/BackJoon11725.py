#1번 노드를 제외한 나머지 노드의 부모를 찾아 출력하는 문제

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
Tree = [[] for _ in range(n+1)]
Parent = [-1] * (n+1)

for _ in range(n-1):
    s,e = map(int,input().split())
    Tree[s].append(e)
    Tree[e].append(s)
#count = 0
    
def DFS(v):
    for i in Tree[v]:
        if Parent[i] == -1:
            Parent[i] = v
            DFS(i)
            #count+=1
            
DFS(1)
for i in range(2,n+1):
    print(Parent[i])
    