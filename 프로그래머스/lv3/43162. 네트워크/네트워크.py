def dfs(visited, cur, n, computers):
    for i in range(0, n):
        if computers[cur][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(visited, i, n, computers)
    return

def solution(n, computers):
    visited = [0 for _ in range(n)]
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            answer += 1
            dfs(visited, i, n, computers)
            
        if 0 not in set(visited):
            break
    
    return answer