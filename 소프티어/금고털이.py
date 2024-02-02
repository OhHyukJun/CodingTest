'''
배낭은 W kh까지 담을 수 있다
각 금속의 무게와 무게당 가격이 주였을 때 배낭을 채울 수 있는 가장 비싼 금액
전기톱으로 자르면 잘려진 부분의 무게만큼 가치를 가진다
1 ≤ N ≤ 10^6인 정수
1 ≤ W ≤ 10^4인 정수
1 ≤ Mi, Pi ≤ 10^4인 정수
입력 예시 
100 2
90 1
70 2

출력 예시
170
'''
import sys

W, N = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

arr.sort(key = lambda x : -x[1])

answer = 0

for i in range(N):
    if W - arr[i][0] >= 0:
        W -= arr[i][0]
        answer += arr[i][0] * arr[i][1]
    else:
        answer += (W * arr[i][1])
        break

print(answer)