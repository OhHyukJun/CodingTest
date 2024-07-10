from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    for i in words:
        count = 0
        target_count = 0
        for j in range(len(i)):
            if begin[j] == i[j]:
                count += 1
            if begin[j] == target[j]:
                target_count += 1
        if target_count == len(i) - 1:
            continue
        if count == len(i) - 1:
            begin = i
            answer += 1
        else: 
            continue
        
    return answer+1