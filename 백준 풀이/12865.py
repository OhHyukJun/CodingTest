'''
N개의 물건
무게 W 가치 V
무게 K는 배낭의 최대값
첫줄 1<=N<=100, 1<=K<=100,000
N개의 줄에 1<=W<=100,000,1<=V<=1,000 
4 7
6 13
4 8
3 6
5 12

14
'''
import itertools
import sys
#input = sys.stdin.readline()

N,K = map(int,input().split())

arr = {}
W_arr = []
for _ in range(N):
    W, V = map(int,input().split())
    arr[W] = V
    W_arr.append(W)
''''
arr = []
W_arr = []
for _ in range(N):
    W, V = map(int,input().split())
    arr.append((W,V))
    W_arr.append(W)
'''
List = []
for i in range(1,len(W_arr)+1):
    for temp in itertools.combinations(W_arr, i):
        if sum(temp) <= K:
            values = [arr[weight] for weight in temp]  # temp의 각 요소에 해당하는 가치를 리스트로 만듦
            if len(temp) == 1:
                List.extend(values)  # values 리스트 전체를 List에 추가
            else: List.append(sum(values))

print(max(List))


