import sys
input = sys.stdin.readline
N = int(input()) #input 값을 저장할 변수
Result=0
A = list(map(int,input().split())) #숫자 데이터를 저장할 리스트 A
A.sort() #리스트 A 정렬

for k in range(N): #숫자만큼 반복
    find = A[k]
    i = 0
    j = N-1
    while i<j: # 투 포인터 알고리즘
        if A[i]+A[j]==find: #두 수의 합이 현재 값과 같다면
            if i!=k and j!=k:
                Result+=1
                break
            elif i==k:
                i+=1
            elif j==k:
                j-=1
        elif A[i]+A[j]<find:
            i+=1
        else:
            j-=1

print(Result)