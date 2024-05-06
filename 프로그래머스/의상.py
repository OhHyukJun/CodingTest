def solution(clothes):
    answer = 1
    arr = {}
    for cloth, kind in clothes:
        if kind in arr.keys():
            arr[kind] += [cloth]
        else:
            arr[kind] = [cloth]
            
    #print(arr.values())
    for i in arr.values():
        answer *= len(i) + 1
    #print(answer)
    return answer-1