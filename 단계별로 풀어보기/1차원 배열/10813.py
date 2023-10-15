N,M = map(int,input().split())
temp = 0
A = []
for i in range(N):
    A.append(i+1)

for i in range(M):
    i,j = map(int,input().split())
    temp = A[i-1]
    A[i-1] = A[j-1]
    A[j-1] = temp
    
for i in range(N):
    print(A[i],end=" ")