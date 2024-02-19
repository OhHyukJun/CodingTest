def solution(name,yearing,photo):
    answer=[]
    sum=0
    play_dict = dict(zip(name,yearing))
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in play_dict.keys():
                sum += play_dict.get(photo[i][j])
        answer.append(sum)
        sum=0
    return answer