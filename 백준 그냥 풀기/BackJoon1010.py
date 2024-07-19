n = int(input())
arr = []
answer = []
for i in range(n):
    N,M = map(int,input().split())
    arr.append((N,M))

for i in arr:
    if i[0] == i[1]:
        answer.append(1)
    else:
        temp = 1
        temp1 = 1
        for j in range(i[1]-i[0]+1,i[1]+1):
            temp *= j
        for k in range(1,i[0]+1):
            temp1 *= k
        answer.append(temp//temp1)

for i in answer:
    print(i)