R, S = input().split()
N = int(str(R)[::-1])
K = int(str(S)[::-1])
if N >K:
    print(N)
else:
    print(K)