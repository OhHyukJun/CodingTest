def solution(brown, yellow):
    answer = []
    sum = brown+yellow
    for i in range(1,sum//2+1):
        if sum % i == 0 and i >= sum//i and sum/i > 2 and int((i*2+(sum/i-2)*2)) == brown:
            answer = (i,sum/i)
            
    return answer