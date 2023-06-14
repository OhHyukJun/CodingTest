#선택 정렬
#대상 데이터에서 최대나 최소 데이터를 데이터가 나열된 순으로 찾아가며 선택하는 방법
#구현 방법이 복잡하고 시간복잡도도 효율적이지 않아 코딩테스트에서 많이 사용하지 않음
#최솟값 또는 최댓값을 찾고, 남은 정렬 부분의 가장 앞에 있는 데이터와 swap하는 것이 핵심


import sys
out = sys.stdout.write #값을 출력할 때 사용
A = list(input())
N = len(A)

for i in range(N):
    Max = i
    for j in range(i+1,N):
        if A[j]>A[Max]: #오름차순일 경우에는 최솟값을 찾는다
            Max=j 
    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp # 두 값을 바꿔준다
for i in range(N):
    out(A[i])
