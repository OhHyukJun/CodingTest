import sys
input = sys.stdin.readline
result = 0

def merge_sort(s,e):
    global result
    if e-s < 1: return #초기 값과 끝 값이 같아지면 종료
    m = int(s+(e-s)/2) #중간값 m을 선언
    merge_sort(s,m) #앞 부분 정렬
    merge_sort(m+1,e) #뒷 부분 정렬
    for i in range(s,e+1): #tmp 배열 선언
        tmp[i] = A[i]
    k=s
    index1 = s
    index2 = m+1    
    while index1 <= m and index2 <=e: # k 값을 왼쪽 오른쪽으로 이동시키는 반복문
        if tmp[index1] > tmp[index2]: #뒤 쪽 데이터가 더 작으면
            A[k] = tmp[index2]
            result = result + index2 - k #뒤 쪽의 데이터가 더 작으면 result값 업데이트
            k+=1
            index2+=1
        else: #뒤 쪽 데이터가 더 크면 앞쪽 인덱스를 증가시켜줌 
            A[k] = tmp[index1]
            k+=1
            index1+=1
    while index1 <= m: #앞 쪽 인덱스가 중간값에 다다르면
        A[k] = tmp[index1]
        k+=1
        index1+=1
    while index2 <= e:
        A[k] = tmp[index2]
        k+=1
        index2+=1

N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
tmp = [0]*int(N+1)
merge_sort(1,N)
print(result)