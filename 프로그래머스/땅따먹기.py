def solution(land):
    n = len(land)
    
    for i in range(1,n):
        for j in range(4):
            max_value = 0
            for k in range(4):
                if k != j:
                    max_value = max(max_value,land[i-1][k])
            land[i][j] += max_value
            
    return max(land[-1])