import sys
input = sys.stdin.readline
N=int(input())
M=int(input())

A = list(map(int,input().split()))
A.sort() #정렬하기
count=0 
i=0 #첫 포인터
j=N-1 #끝 포인터

# while i<j:
#     if 재료 합 < M: 작은 번호 재료를 한 칸 위로 변경
#     elif 재료 합 > M: 큰 번호 재료를 한 칸 아래로 변경
#     else 경우의 수 증가, 양쪽 index 각각 변경

while i<j:
    if A[i]+A[j] < M:
        i += 1
    elif A[i]+A[j] >M:
        i -= 1
    else:
        count+=1
        i+=1
        j+=1

print(count)  


