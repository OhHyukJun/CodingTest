from collections import deque

def solution(dartResult):
    answer = 0
    darResult = list(dartResult)
    #print(darResult)
    arr = []
    nums = ['1','2','3','4','5','6','7','8','9','0']
    queue = deque()
    for i in range(len(darResult)):
        num = darResult.pop(0)
        if num in nums and darResult[0] in nums:
            num = num + darResult.pop(0)
            darResult.append(num)
        else:
            darResult.append(num)
    #print(darResult)
    for i in range(len(darResult)):
        if darResult[i] == 'S':
            arr.append(int(darResult[i-1])**1)
        elif darResult[i] == 'D':
            arr.append(int(darResult[i-1])**2)
        elif darResult[i] == 'T':
            arr.append(int(darResult[i-1])**3)
        elif darResult[i] == '#':
            arr[-1] = arr[-1]*(-1)
        elif darResult[i] == '*':
            if len(arr) > 1:
                arr[-1] = arr[-1] * 2
                arr[len(arr)-2] = arr[len(arr)-2] * 2
            else:
                arr[-1] = arr[-1] * 2
    #print(arr)
    for i in arr:
        answer += i
    return answer