def solution(operations):
    answer = []
    arr=[]
    for i in operations:
        arr.append(i.split())
    for i in arr:
        if i[0] == 'I':
            answer.append(int(i[1]))
        elif i[0] == 'D' and int(i[1]) == -1 and len(answer) != 0:
            answer.remove(min(answer))
        else:
            if len(answer) != 0:
                answer.remove(max(answer))

    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer),min(answer)]
