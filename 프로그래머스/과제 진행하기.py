def solution(plans):
    answer = []
    arr = []
    plans.sort(key=lambda x : x[1])
    
    for plan in plans:
        h, m = map(int, plan[1].split(':'))
        plan[1] = h * 60 + m
        plan[2] = int(plan[2])
    
    for i in range(len(plans)-1):
        arr.append([plans[i][0],plans[i][2]])
        gap = plans[i+1][1] - plans[i][1]
        while arr and gap:
            if arr[-1][1] <= gap:
                before,after = arr.pop()
                gap -= after
                answer.append(before)
            else:
                arr[-1][1] -= gap
                gap = 0
                
    answer.append(plans[-1][0])
    
    for i in range(len(arr)):
        answer.append(arr[len(arr)-i-1][0])
    
    return answer