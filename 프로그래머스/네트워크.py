def solution(n, computers):
    answer = 0
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == 0:
                dfs(j)
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1

    return answer