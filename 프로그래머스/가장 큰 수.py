'''
0 1 2
0 2 1
1 0 2
1 2 0
2 0 1
2 1 0
'''
from itertools import permutations

def solution(numbers):
    n = len(numbers)
    answer = ''
    if numbers.count(0) == n:
        return '0'
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x:x*3, reverse=True)
    
    for i in range(n):
        answer+=numbers[i]
    return answer