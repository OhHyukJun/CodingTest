def solution(n, k):
    answer = 0
    trans_n = ''
    
    while n > 0:
        n, mod = divmod(n,k)
        trans_n += str(mod)
        
    trans_n = trans_n[::-1].split('0')
    
    for i in trans_n:
        count = 0
        if len(i) == 0 or int(i) < 2:
            continue
        else:
            for j in range(2,int(i,k)//2+1):
                if int(i) % j == 0:
                    count +=1
                    break
        if count == 0:
            answer += 1
    return answer
