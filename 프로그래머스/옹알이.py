def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    i=0
    while i < len(babbling):
        for j in range(4):
            if arr[j] in babbling[i]:
                babbling[i]=babbling[i].replace(arr[j],' ')
        if babbling[i] not in arr:
            i += 1
        else:
            i += 1

    for i in babbling:
        if i.isspace() == True:
            answer += 1
                   
    return answer