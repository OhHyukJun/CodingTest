def solution(s, skip, index):
    answer = ''
    arr =[]
    s = list(s)

    for i in range(len(skip)):
        arr.append(skip[i])
    for i in range(len(s)):
        count = 0
        current = s[i]
        while count < index:
            current = chr((ord(current)-ord('a')+1)%26+ord('a'))
            if current in skip:
                continue
            count += 1
        answer += current
    return answer