#삽입 정렬
#이미 정렬된 데이터 범위에 정렬되지 않은 데이터를 적적한 위치에 삽입시켜 정렬하는 방식 시간복잡도는 O(n^2)으로 느린 편이지만 구현하기가 쉽다
#선택 데이터를 현재 정렬된 데이터 범위 내에서 적절한 위치에 삽입하는 것이 삽입 정렬의 핵심

#1. 현재 index에 있는 데이터 값을 선택
#2. 현재 선택한 데이터가 정렬된 데이터 범위에 삽입될 위치를 탐색함
#3. 삽입 위치부터 index에 있는 위치까지 shift 연산을 수행함
#4. 삽입 위치에 현재 선택한 데이터를 삽입하고 index++ 연산을 수행함
#5. 전체 데이터의 크기만큼 index가 커질 때까지, 즉 선택할 데이터가 없을 때까지 반복함

#그리디 방식으로 문제에 접근 
#사람 수 - 자릿 수 별로 정리한 리스트 - 각 사람이 인출하는데 필요한 시간을 저장
# 3 1 4 3 2 3 - 4 - 8 11 13 32
N = int(input())
A = list(map(int,input().split())) #각 값을 리스트로 나눠주기 위해 사용
S = [0]*N #각 사람이 인출하는데 드는 시간을 저장

for i in range(1,N):
    in_point =i 
    in_value =A[i]
    for j in range(i-1,-1,-1):
        if A[j] < A[i]: #앞의 값보다 크다면
            in_point = j+1
            break
        if j==0:
            in_point = 0
    for j in range(i,in_point,-1):
        A[j] = A[j-1] #정렬하기
    A[in_point] = in_value
     
S[0] = A[0]

for i in range(1,N):
    S[i]=S[i-1]+ A[i] #시간의 합 배열 구하기

sum = 0

for i in range(0,N):
    sum+=S[i] #합 배열 총합 구하기

print(sum)
