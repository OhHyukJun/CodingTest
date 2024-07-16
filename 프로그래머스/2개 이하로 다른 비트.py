def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i+1)
        else:
            i = '0' + bin(i)[2:]
            i = list(i)
            one_index = 0
            for j in range(len(i)):
                if i[j] == '0':
                    one_index = j
            i[one_index+1] = '0'
            i[one_index] = '1'
            answer.append(int("".join(i),2))
    return answer