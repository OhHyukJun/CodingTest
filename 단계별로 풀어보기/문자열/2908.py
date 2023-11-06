S,R = input().split()
N = int(str(S)[::-1])
T = int(str(R)[::-1])
if(N>T):
    print(N)
else:
    print(T)