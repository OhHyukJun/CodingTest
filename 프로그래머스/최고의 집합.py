def solution(n, s):
    answer = []
    arr = []
    if n > s:
        return [-1]
    for _ in range(n):
        arr.append(s//n)
    
    k = len(arr) - 1
    if sum(arr) < s:
        for i in range(s-sum(arr)):
            arr[k-i] += 1
            
    arr.sort()
    return arr