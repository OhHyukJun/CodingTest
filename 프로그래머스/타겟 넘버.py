'''적절한 더하기 빼기를 사용하자
2 <= len(numbers) <=20
1 <= numbers[i] <= 50
1 <= target <= 1000
4 1 2 1 -> 4
4 -1 +2 -1 -> 4
4 1 -2 1 -> 4
'''

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        number,index = queue.popleft()
        index+=1
        if index < n:
            queue.append([number+numbers[index],index])
            queue.append([number-numbers[index],index])
        else:
            if number == target:
                answer += 1
            
    return answer