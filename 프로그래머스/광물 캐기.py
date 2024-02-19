def solution(picks, minerals):
    answer = 0
    sum = picks[0] + picks[1] + picks[2]
    
    num_min = sum * 5
    
    if num_min < len(minerals):
        minerals = minerals[:num_min]
    
    new_minerals = [[0,0,0] for _ in range(len(minerals)//5 + 1)]
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i//5][0] += 1 #다이아몬드 개수 세기
        elif minerals[i] == 'iron': 
            new_minerals[i//5][1] += 1 #철 개수 세기
        else:
            new_minerals[i//5][2] += 1 #돌 개수 세기
    
    new_minerals=sorted(new_minerals, key=lambda x : (-x[0], -x[1], -x[2])) 
		# 다이어 철 돌 정렬하기
    
    for i in new_minerals:
        dia, iron, stone = i
        for pick in range(3):
            if pick == 0 and picks[pick] > 0:
                picks[pick] -= 1
                answer += dia + iron + stone
                break
            elif pick == 1 and picks[pick] > 0:
                picks[pick] -= 1
                answer += 5*dia + iron + stone
                break
            elif pick == 2 and picks[pick]:
                picks[pick] -= 1
                answer += 25*dia + 5*iron +stone
                break
    return answer