def solution(skill, skill_trees):
    answer = 0
    n = len(skill_trees)
    arr=[[] for _ in range(n)]
    skill = list(skill)
    for i in range(n):
        skill_trees[i] = list(skill_trees[i])
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                arr[i].append(skill_trees[i][j])
    for i in arr:
        temp = 0
        for j in range(len(i)):
            if i[j] == skill[j]:
                temp += 1
        if temp == len(i):
            answer += 1
            
    return answer