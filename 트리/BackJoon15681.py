import sys
sys.setrecursionlimit(10**9)
#반복제한 늘리기
N,R,Q = map(int,sys.stdin.readline().split())
#입력받기

Tree =[[] for _ in range(N+1)] #이진 트리 초기화
visit = [-1 for _ in range(N+1)] #방문 배열

for _ in range(N-1):
    s,e = map(int,sys.stdin.readline().split())
    Tree[s].append(e)
    Tree[e].append(s)
    
def dfs(now):
    global visit
    visit[now] = 1 #나 자신을 추가해줌
    for i in Tree[now]:
        if visit[i] == -1: #방문하지 않은 방문 가능 노드가 있으면
            visit[now]+=dfs(i) #방문하며 그 노드의 서브트리 개수를 더함
    return visit[now] #내 서브트리 개수를 return 루트 노드에 가면 모든 서브트리의 개수 출력

dfs(R)

for _ in range(Q):
    get = int(sys.stdin.readline())
    print(visit[get]) #정답 출력