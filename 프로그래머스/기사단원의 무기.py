'''
제곱수
자기자신
'''
def solution(number, limit, power):
    answer = 0
    arr = []
    for i in range(number):
        arr.append(i+1)
    for i in arr:
        temp = 0
        for j in range(1,int(i**0.5)+1):
            if i % j == 0 and j*j != i:
                temp += 2
            elif i % j == 0 and j*j == i:
                temp += 1
            elif i == j:
                temp += 1
        if temp > limit:
            temp = power
        answer += temp

    return answer