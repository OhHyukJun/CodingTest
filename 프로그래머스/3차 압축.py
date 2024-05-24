def solution(msg):
    answer = []
    msg = list(msg)
    n = len(msg)
    check = {}
    for i in range(26):
        check[chr(65+i)] = i+1
    
    index = 27
    i = 0
    while i<n:
        w = msg[i]
        while i < n-1 and w + msg[i+1] in check:
            w += msg[i+1]
            i += 1
            
        answer.append(check[w])
        if i < n-1:
            check[w+msg[i+1]] = index
            index+=1
        i+=1
    #print(check)
    return answer