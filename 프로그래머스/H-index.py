def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    for i in range(n):
        if i >= citations[i]:
            return i
        
    return n