# 숫자의 개수와 질문의 개수를 정의
# 숫자데이터를 변수에 저장
# 배열 선언
# temp 변수 선언
# temp에 숫자 데이터를 더하기
# 질문의 개수만큼 더하기

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))
sum = [0]
temp = 0

for i in num:
    temp = temp+i
    sum.append(temp)

for i in range(M):
    s,e=map(int,input().split())
    print(sum[e]-sum[s-1])