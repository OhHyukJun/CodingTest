def solution(s):
    balance = 0  
    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        elif s[i] == ')':
            balance -= 1
        if balance < 0:
            return False
        
    if balance == 0:
        return True
    else: 
        return False
    
