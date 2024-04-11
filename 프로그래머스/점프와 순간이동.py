def solution(n):
    ans = 0
    '''1 점프 -> 2로 이동 -> 4로 이동 -> 1 점프 = 5 = 2
    2 점프 -> 4로 이동 -> 6로 이동 = 2'''
    while True:
        if n % 2 != 0:
            n-=1
            ans+=1 
        n = n // 2
        if n < 1:
            break
    
    return ans