import sys

N, C = map(int,sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)

start, end = 1, arr[-1] - arr[0]

while start <= end:
    mid = (start+end) // 2
    distance = arr[0]
    machine = 1
    for i in arr:
        if i >= distance + mid:
            distance = i
            machine += 1
    if machine >= C:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)
