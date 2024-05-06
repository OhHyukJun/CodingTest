def solution(s):
    
    s = s.strip('{}').split('},{')
    s = [list(map(int,s.split(','))) for s in s]
    s = sorted(s,key=len)
    
    answer = s[0]
    
    for i in range(1,len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in s[i-1]:
                answer.append(s[i][j])
                
    return answer
    
    
    

