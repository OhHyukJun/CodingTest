def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            hab = numbers[i]+numbers[j]
            if hab not in answer:
                answer.append(hab)
    answer.sort()
    return answer