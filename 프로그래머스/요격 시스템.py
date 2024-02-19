def solution(targets):
    targets.sort(key = lambda x: x[1])  # 끝점을 기준으로 정렬
    answer= 0
    end = -1
    for target in targets:
        if target[0] >= end:  # 현재 요격 미사일이 커버할 수 없는 범위일 경우
            end = target[1]  # 새로운 요격 미사일 사용
            answer+= 1
    return answer