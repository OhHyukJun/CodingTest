n = int(input())
arr = list(map(int, input().split()))

answer = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            answer[i] = max(answer[i],answer[j]+1)
            
print(max(answer))