def solution(want, number, discount):
    answer = 0
    arr = []
    i = 0
    while i < len(discount)-9:
        count = 0
        arr = discount[i:10+i]
        for j in range(len(want)):
            if number[j] - arr.count(want[j]) <= 0:
                count += 1
        if count == len(want):
            answer+=1
        i+=1
            
    return answer