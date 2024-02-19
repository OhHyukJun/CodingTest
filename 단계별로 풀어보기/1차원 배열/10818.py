N = int(input())
A = list(map(int,input().split()))
min=A[0]
max=A[0]

for i in range(N):
    if(min>A[i]):
        min = A[i]
    if(max<A[i]):
        max = A[i]
        
print (min,max)