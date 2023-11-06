#N장의 카드 - 1~N 1번 카드가 가장 위 N번이 가장 아래 = deque
#가장 위의 카드를 바닥에 버린다 -> 그 다음 카드를 제일 밑으로 -> 가장 위를 버린다 ...
# 1 2 3 4 -> 2 3 4 -> 3 4 2 -> 4 2 -> 2 4 -> 4

from collections  import deque
N = int(input())
myQueue = deque()

for i in range(1,N+1):
    myQueue.append(i)
    
while len(myQueue) > 1:
    myQueue.popleft() #맨 위의 값을 버림
    myQueue.append(myQueue.popleft()) #그 다음 값을 가장 아래에 추가한다
    
print(myQueue[0]) #마지막 값을 출력한다