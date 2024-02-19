N=0
index=0
for i in range(9):
    A=int(input())
    if(N<A):
        N=A
        index=i+1

print(N)
print(index)