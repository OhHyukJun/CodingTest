def solution(n):
    answer = 0
    count_one = format(n,'b').count('1')
    while True:
        n+=1
        count = format(n,'b').count('1')
        if count == count_one:
            answer = n
            break
    return answer