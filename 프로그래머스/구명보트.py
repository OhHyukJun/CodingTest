from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    queue = deque(people)
    
    while len(queue) > 0:
        if len(queue) == 1:
            queue.pop()
            answer += 1
        elif queue[0] + queue[-1] <= limit:
            answer += 1
            queue.pop()
            queue.popleft()
        else:
            if len(queue) != 0:
                answer += 1
                queue.popleft()
    #print(queue)
    return answer