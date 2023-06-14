#퀵 정렬
# pivot을 선정해 해당 값보다 작은 데이터아 큰 데이터로 분류하는 작업을 반복해 정렬하는 알고리즘
# pivot이 어떻게 선정되는지가 시간 복잡도에 많은 영향을 미치고, 평균적으로는 O(nlogn)이며 최악의 경우에는 O(n^2)의 복잡도를 갖는다

#1. 데이터를 분할하는 pivot을 설정함
#2. pivot을 기준으로 다음의 과정을 거쳐 데이터를 2개의 집합으로 분히
   # 2-1 start가 가리키는 데이터가 pivot이 가리키는 데이터보다 작으면 start를 오른쪽으로 1칸 이동한다
   # 2-2 end가 가리키는 데이터가 pivot이 가리키는 데이터보다 크면 end를 왼쪽으로 1칸 이동한다
   # 2-3 start가 가리키는 데이터가 pivot이 가리키는 데이터보다 크고, end가 가리키는 데이터가 pivot이 가리키는 데이터보다 작으면
   #     start,end가 가리키는 데이터를 swap하고 start는 오른쪽,end는 왼쪽으로 1칸씩 이동한다
   # 2-4 start,end가 만날 때 까지 위의 과정을 반복
   # 2-5 start,end가 만나면 만난 지점에서 가리키는 데이터와 pivot이 가리키는 데이터를 비교하여 
   #     pivot > 가리키는 데이터이면 만난 지점의 오른쪽에 작으면 pivot이 가리키는 데이터를 삽입한다
#3. 분리 집합에서 각각 다시 pivot을 선정하여 분리 집합이 1개 이하일 때까지 과정을 반복한다.

import sys
input = sys.stdin.readline
N,K = map(int,input().split()) #N: 숫자의 수 K: K번째 수
A = list(map(int,input().split())) #숫자 데이터 저장 배열

def quickSort(S,E,K):
    global A
    if S<E:
        pivot = partition(S,E)
        if pivot == K: # K번째 수가 pivot이면 중지
            return
        elif K < pivot: # K가 pivot보다 작으면 왼쪽 그룹만 정력
            quickSort(S,pivot-1,K)
        else: #K가 pivot보다 크면 오른쪽 그룹 정렬
            quickSort(pivot+1,E,K)
def swap(i,j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
def partition(S,E):
    global A
    
    if S+1 == E:
        if A[S] > A[E]:
            swap(S,E)
        return E
    
    M = (S + E) //2
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E
    while i <= j:
        while pivot < A[j] and j > 0:
            j = j-1 #피벗값보다 작은 수가 나올 때까지 j를 감소
        while pivot > A[i] and i < len(A) -1:
            i= i+1 #피벗값보다 큰 수가 나올 때까지 i를 증가
        if i <= j:
            swap(i,j)
            i=i+1
            j=j-1    
    A[S] = A[j]
    A[j] = pivot
    return j

quickSort(0,N-1,K-1)
print(A[K-1])
            
            
