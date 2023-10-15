import sys
T = int(sys.stdin.readline())
for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    print('Case #'+str(i+1)+': '+str(a+b))