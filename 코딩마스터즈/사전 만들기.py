import sys 

n = int(input())
arr = []
length = []
for _ in range(n):
    arr.append((input()))
arr = sorted(arr,key=lambda x:(len(x),x))
print(arr)
