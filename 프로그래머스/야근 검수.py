import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    
    works = [-i for i in works]
    works.sort()

    while n > 0:
        temp = heapq.heappop(works)
        heapq.heappush(works, temp+1)
        n -= 1

    for i in works:
        answer += i**2
    
    return answer