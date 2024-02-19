#1. 뒤에서부터 확인하며 삽입하려는 요소보다 큰 값들을 제거
#2. 앞에서부터 보며 슬라이딩 범위를 벗어난 요소들을 제거
#3. 현재 요소 삽입

#N개의 수와 L이 주어진다 N개의 수의 최솟 값을 D 이 때 D를 출력
from collections import deque #deque import 방법
import sys

N,L = map(int,input().split()) # N: 숫자의 개수, L: 최솟값을 구하는 범위
a = deque() #데이터를 담을 덱 자료구조

array = list(map(int,input().split())) #주어진 숫자 데이터를 가지는 리스트

for i in range(N):
    while a and a[-1][0] > array[i]:
        a.pop() #오른쪽 끝 요소를 불러옴과 동시에 삭제
    a.append((array[i],i))
    if a[0][1] <= i - L: #범위에서 벗어나는 값을 제거
        a.popleft() #덱의 왼쪽 끝 요소를 가져옴과 동시에 덱에서 삭제
    print(a[0][0],end=' ')
    