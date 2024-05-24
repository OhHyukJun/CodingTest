from itertools import permutations
        
def solution(numbers):
    answer = 0
    arr = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            num = int(''.join(j))
            if num != 1 and num != 0:
                arr.add(num)
    for i in arr:
        for j in range(2,i//2+1):
            if i % j == 0:
                answer += 1
                break
    #print(arr)
    return len(arr) - answer