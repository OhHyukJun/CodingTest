import sys 
arr = list(map(str,input().split()))
answer = ''
for i in range(len(arr)):
    if arr[i] == 'c':
        answer += 'c'
        break
    else:
        answer += arr[i]+' '
        
print(answer)