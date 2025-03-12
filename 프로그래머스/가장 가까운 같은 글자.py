def solution(s):
    answer = []
    s = list(s)
    arr = []
    for i in range(len(s)):
        k = s.pop(0)
        if k not in arr:
            answer.append(-1)
        else:
            temp = list(reversed(arr))
            answer.append(temp.index(k)+1)
        arr.append(k)
    return answer