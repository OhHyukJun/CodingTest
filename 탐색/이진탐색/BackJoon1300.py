'''
    이 문제는 이진탐색으로 푸는 문제이다
'''
import sys
N = int(input())
K = int(input())
start = 1
end = K #k번 째 수는 k보다 클 수 없기 때문
ans = 0

while start <= end: #start와 end가 같아지면 middle에 도달한 것
    middle = int((start+end)/2) #B[K] 값으로 찾을 값
    count = 0 #중앙값을 받아올 count
    for i in range(1,N+1):
        count += min(int(middle/i),N) #중앙값을 더해감
        if count < K:
            start = middle + 1
        else:
            ans = middle
            end = middle - 1
            
print(ans)