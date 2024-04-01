def solution(weights):
    weight_dict = dict()
    answer = 0
    
    for i in weights:
        if i in weight_dict:
            weight_dict[i] += 1
        else:
            weight_dict[i] = 1
    
    for i in weights:
        if i % 2 == 0:
            target = i * 3 // 2
            if target in weight_dict:
                answer += weight_dict[target]
        if i % 3 == 0:
            target = i * 4 // 3
            if target in weight_dict:
                answer += weight_dict[target]
        target = i * 2
        if target in weight_dict:
            answer += weight_dict[target]
    
    for i in weights:
        weight_dict[i] -= 1
        answer += weight_dict[i]
    print(weight_dict)
    return answer

    