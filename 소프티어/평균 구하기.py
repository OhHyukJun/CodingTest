'''
제약조건
1<=N<=10^6
1<=K<=10^4
1<=Si<=100
1<=Ai<=Bi<=N
입력형식
학생 수:N, 구간 수:K
두 번째 줄에는 학생의 성적 Si i+2 번째 줄에는 i번째 구간 A,B가 주어짐
출력형식
i번째 줄에 i번째 구간의 성적평균을 출력한다. 차이가 0.01이하이면 정답으로 채점됨
'''

import sys
N,K = map(int,input().split())
arr = list(map(int,input().split()))
grade = []
for _ in range(K):
    a,b = map(int,input().split())
    grade.append((a,b))

for i in range(K):
    temp = 0
    for j in range(grade[i][0]-1,grade[i][1]):
        temp += arr[j]
    print("{:.2f}".format(temp/(grade[i][1]-grade[i][0]+1)))