def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j] #각 행의 1번 째 값들의 합
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1] #각 행의 마지막 값들의 합
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]) #왼쪽 오른쪽 값들을 더함
    answer = max(triangle[-1]) # 제일 마지막 줄에서 최대값을 답으로 출력
    
    return answer