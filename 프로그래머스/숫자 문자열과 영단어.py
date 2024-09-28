def solution(s):
    answer = ''
    alpha = ['zero','one','two','three','four','five','six','seven','eight','nine']
    num = ['0','1','2','3','4','5','6','7','8','9']
    s = list(s)
    temp = ''
    for i in range(len(s)):
        if s[i] not in num:
            temp += s[i]
        elif s[i] in num:
            answer += s[i]
        if temp in alpha:
            answer += str(alpha.index(temp))
            temp = '' 
    
    return int(answer)