from collections import deque

def solution(tickets):
    answer = []
    queue = deque()
    queue.append(('ICN',[],[]))
    
    while queue:
        now, next, visit = queue.popleft()
        
        if len(visit) == len(tickets):
            answer.append(next)
        
        for idx, ticket in enumerate(tickets):
            if now == ticket[0] and not idx in visit:
                if next == []:
                    queue.append((ticket[1], next +[ticket[0]] + [ticket[1]], visit + [idx]))
                else:
                    queue.append((ticket[1], next + [ticket[1]], visit + [idx]))
    answer.sort()
    return answer[0]