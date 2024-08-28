def solution(s):
    s = list(s)
    arr = []
    x = s[0]
    str = s[0]
    yes = 1
    no = 0
    i=0
    
    while True:
        i += 1
        if i == len(s):
            arr.append(s[-1])
            break
        if x == s[i]:
            yes += 1
            str += s[i]
        else: 
            no += 1
            str += s[i]
        if yes == no:
            arr.append(str)
            i += 1
            if i == len(s):
                break
            yes = 1
            no = 0
            x = s[i]
            str = s[i]
            
    return len(arr)