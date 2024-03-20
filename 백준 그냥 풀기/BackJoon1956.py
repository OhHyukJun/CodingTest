'''
ABCD 2143 -> CDAB 출력
우선순위가 있는 녀석을 가장 앞으로! 그러면서 그 우선순위 앞의 녀석들을 뒤로 이동해야하지

'''
from collections import deque

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    
    queue = deque([(value,idx) for idx, value in enumerate(arr)])

    count = 0
    
    while queue:
        current = queue.popleft()
        
        if current[0] < max(queue, key=lambda x: x[0])[0]:
            queue.append(current)
        else:
            count += 1
            if current[1] == b:
                print(count)
                break