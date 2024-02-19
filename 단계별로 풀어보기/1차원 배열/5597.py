N = []
for i in range(30):
    N.append(i+1)
    
for _ in range(28):
    a = int(input())
    N.remove(a)
    
print(min(N))
print(max(N))