'''
    i,j번 레슨을 같은 블루레이에 녹화하려면 사이의 모든 레슨도 같은 블루레이로 녹화해야 함
'''

N,M = map(int,input().split())
A= list(map(int,input().split()))
start = 0
end = 0

for i in A:
    if start < i:
        start = i #레슨 최댓값을 시작 인덱스로 저장
    end += i #모든 레슨의 총합을 종료 인덱스로 저장

while start <= end:
    middle = int((start+end)/2) #중간 인덱스
    sum = 0 #레슨 합
    count = 0 #현재 사용한 블루레이의 개수
    for i in range(N): # 중간값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + A[i] > middle: #현재 레슨 시간 + sum이 중간값보다 크면
            count += 1 #count 증가
            sum = 0 #sum 초기화
        sum += A[i] #sum에 현재 레슨 시간값 더하기
    if sum != 0:
        count += 1 #sum이 0이 아니면 count 증가
    if count > M: # 중간 인덱스값으로 모든 레슨 저장 불가능
        start = middle + 1
    else:
        end = middle -1
    
print(start)    
    