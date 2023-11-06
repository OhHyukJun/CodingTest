import sys
input = sys.stdin.readline
#반복문으로 여러줄을 입력 받아야 할 때 사용
#그냥 input으로 받으면 시간초과가 발생할 수 있음
n,m = map(int,input().split()) # 리스트 크기와 질문의 수
#input().split(): 한 번에 여러 개의 입력값을 받음 
A = [[0]*(n+1)] #원본 리스트
D = [[0]*(n+1) for _ in range(n+1)] #합 배열
# 반복문에서 _를 사용하는 경우
# 1.인터프리터에 마지막 값을 저장하고 싶을 때
# 2.값을 무시하고 싶을 때
# 3.변수나 함수 명에 의미를 부여하고 싶을 때
# 4.숫자 리터럴 값의 자릿수 구분을 위한 구분자로 사용할 때
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
    
for i in range(1,n+1):
    for j in range(1,n+1):
        #합 배열 저장
        D[i][j] = D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i][j]
 
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2]-D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)

