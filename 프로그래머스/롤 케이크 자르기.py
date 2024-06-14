from collections import Counter

def solution(topping):
    bro_topping = Counter()
    young_topping = Counter(topping)
    answer = 0
    
    for i in topping:
        bro_topping[i] += 1
        young_topping[i] -= 1
        
        if young_topping[i] == 0:
            del(young_topping[i])
        if len(bro_topping) == len(young_topping):
            answer += 1
        elif len(bro_topping) > len(young_topping):
            break
    return answer