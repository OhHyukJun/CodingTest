N,M = map(int,input().split())
A = []

for _ in range(N):
    A.append(0)

for _ in range(M):
    i,j,k = map(int,input().split())
    for a in range(i-1,j):
        A[a] = k

for i in range(N):
    print(A[i], end=" ")