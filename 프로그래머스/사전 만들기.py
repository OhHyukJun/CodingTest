import sys 

n = int(input())
arr = []
answer = []
length = []
for _ in range(n):
    arr.append((input()))
arr = sorted(arr,key=lambda x:(len(x),x))
for i in arr:
    if i not in answer:
        answer.append(i)

for i in answer:
    print(i)
