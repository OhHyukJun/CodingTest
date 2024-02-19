import sys
input = sys.stdin.readline()
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(8)]

str1 = ['ascending','descending','mixed']
answer = ''
for i in range(len(arr)):
    k=0
    if arr[0] == 1:
        k = 1
    elif arr[0] == 8:
        k = 8
    else:
        answer = str1[2]
    if k == 1:
        if arr[i] == i+1:
            answer = str1[0]
            continue
    elif k == 8:
        if arr[i] == 8-i:
            answer = str1[1]
            continue
        else: answer = str1[2]
            
print(answer)