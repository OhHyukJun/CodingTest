import sys
input = sys.stdin.readline
#입력의 개수가 많을 때 stdin.readline을 사용하여 계산 속도를 올려줌
n, m = map(int,input().split())
#map함수의 기본형태 map(반복가능한 자료형,적용할 함수)
A = list(map(int,input().split()))
S = [0]*n
C = [0]*m
S[0]=A[0]
answer=0
for i in range(1,n):
    S[i]=S[i-1]+A[i]
for i in range(n):
    remainer = S[i]%m
    if remainer == 0: #0~i까지의 구간 합 자체가 0일 때 정답에 더하기
        answer+=1
    C[remainer]+=1 #나머지가 같은 인덱스의 개수 값 증가시키기
    
for i in range(m):#나머지가 같은 인덱스 중 2개를 뽑는 경우의 수 더하기
    if C[i]>1:
        answer += (C[i]*(C[i]-1)//2)

print(answer)