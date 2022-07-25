visited = [0 for _ in range(200)]

def dfs(cur, n, computers):
    global visited
    for i in range(0, n):
        if computers[cur][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(i, n, computers)
    return

def solution(n, computers):
    global visited
    answer = 0
    
    for i in range(0, n):
        if not visited[i]:
            visited[i] = 1
            answer += 1
            dfs(i, n, computers)
    
    return answer