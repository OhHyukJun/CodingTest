import sys 
from collections import deque

n = int(input())
arr = []
for i in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)

for i in range(1,n):
    for j in range(len(arr[i])):
        if i == j:
            arr[i][j] += arr[i-1][j-1]
        elif i >1 and j<len(arr[i-1]) and j>0:
            arr[i][j] += max(arr[i-1][j],arr[i-1][j-1])
        else:
            arr[i][j] += arr[i-1][j]

print(max(arr[-1]))