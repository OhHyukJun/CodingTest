s = input()
def solution(s):
    answer = len(s)
    N = len(s)

    for j in range(1,N//2+1):
        result = [s[i:i+j] for i in range(0,N,j)]
        temp = ''
        count = 1
        for i in range(1,len(result)):
            if result[i] == result[i-1]:
                count += 1
            else:
                if count > 1:
                    temp += str(count) + result[i-1]
                else:
                    temp += result[i-1]
                count = 1
        if count > 1: #문자열의 마지막 글자를 비교하기 위한 코드
            temp += str(count) + result[-1]
        else:
            temp += result[-1]
        answer = min(answer,len(temp)) 

    return answer

print(solution(s))
