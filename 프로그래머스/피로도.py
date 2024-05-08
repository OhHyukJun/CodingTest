from itertools import permutations
# 피로도 시스템(정수) 최소피로도 소모 피로도
def solution(k, dungeons):
    #answer = -1
    count = 0
    c = list(permutations(dungeons,len(dungeons)))

    #k >= dungeons[0][0] -> k -= dungeons[0][1]
    #n = len(dungeons)
    for i in c:
        temp = 0
        temp_k = k
        for current, use in i:
            if temp_k >= current:
                temp_k -= use
                temp += 1   
        #print(count,temp)
        count = max(count,temp)
        
    return count