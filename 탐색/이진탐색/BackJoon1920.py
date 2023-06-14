'''
    현재 데이터셋의 중앙값을 선택함
    중앙값 > 타겟 데이터이면 중앙값을 기준으로 왼쪽 데이터를 선택
    중앙값 < 타겟 데이터이면 오른쪽 데이터를 선택
    과정을 반복하며 중앙값 === 타겟 데이터이면 종료
'''
N = int(input()) #데이터 개수
A = list(map(int,input().split())) #데이터 리스트 저장
A.sort() #정렬
M = int(input()) #찾아야 하는 수의 개수
target_list = list(map(int,input().split())) #찾아야 하는 데이터 리스트 저장

for i in range(M): 
    find = False
    target = target_list[i] #찾아야 하는 수
    start = 0 #시작점
    end = len(A) - 1 #끝점
    while start <= end: 
        midium = int((start+end)/2) #중간 인덱스
        midium_value = A[midium] #중앙값
        if midium_value > target: #인덱스가 타겟보다 크면
            end = midium - 1 #끝점을 왼쪽으로
        elif midium_value < target:
            start = midium + 1 #시작점을 오른쪽으로
        else: 
            find = True #찾으면 멈춤
            break
    if find:
        print(1)
    else:
        print(0)