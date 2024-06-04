from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices) 
    while queue:
        temp = 0
        price = queue.popleft()
        for i in queue:
            temp+=1
            if i < price:
                break
        answer.append(temp)
    return answer