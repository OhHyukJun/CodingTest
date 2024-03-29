'''
95 90 99 99 80 99
100 95 100 100 85 100 1
95 100 100 85 100
100 100 100 90 100 3
90 100
100 100 2
'''
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while progresses:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
            
    answer.append(count)        
    return answer