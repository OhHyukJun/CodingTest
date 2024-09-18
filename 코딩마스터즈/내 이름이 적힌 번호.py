import sys 

a,b = map(str, input().split())
arr = list(map(str,input().split()))

for i in range(int(a)):
    if arr[i] == b:
        print(i+1)
