cnt=0
N=[]
for _ in range(10):
    x = int(input())
    N.append(x%42)
N=set(N)
print(len(N))
    