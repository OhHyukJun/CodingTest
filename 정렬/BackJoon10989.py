'''
    기수 정렬: 값을 비교하지 않는 정렬 값을 놓고 비교할 자릿루를 정한 후 해당 자릿수만 비교
    시간 복잡도: O(kn)
    10개의 큐를 이용 - 1의 자릿수를 기준으로 데이터 저장 - 정렬 - 십의 자릿수를 기준으로 데이터 저장 - 정렬
    코딩테스트에서 정렬해야 하는 데이터가 많을 때 사용하면 좋음
'''
import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001 #자연수는 10000 이하의 자연수

for i in range(N):
    count[int(input())]+=1 #count 배열에 값 추가

for i in range(10001): #1부터 범위 전체를 반복
    if count[i] != 0:
        for _ in range(count[i]): #index만큼 index를 반복 출력
            print(i)