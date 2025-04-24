from collections import deque

def solution(cards1, cards2, goal):
    for word in goal:
        if len(cards1) != 0 and word == cards1[0]:
            q = deque(cards1.pop(0))
        elif len(cards2) != 0 and word == cards2[0]:
            q = deque(cards2.pop(0))
        else:
            return "No"
        queue = q.popleft()
    return "Yes"