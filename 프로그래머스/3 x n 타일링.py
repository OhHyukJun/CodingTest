def solution(n):
    answer = 0
    result = []
    for i in range(0,n+1):
        if i % 2 == 0:
            if i== 2: 
                result.append(3)
            elif i ==4: 
                result.append(11)
            elif i>4: 
                result.append(result[i//2-2]*4 - result[i//2-3])

    return max(result) % 1000000007