from collections import deque

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
    
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
    
        if x == n-1 and y == m-1:
            return
        
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if in_range(nx, ny, n, m):
                if maps[nx][ny] == 0:
                    continue
                    
                elif maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
                
                else:
                    if maps[nx][ny] > maps[x][y] + 1: # 최단 경로를 갱신할 수 있을 경우
                        maps[nx][ny] = maps[x][y] + 1
                        q.append((nx, ny))

# check range is valid.
def in_range(x, y, n, m):
    if 0<=x<n and 0<=y<m:
        return True
    return False
    
def solution(maps):
    INF = 99999
    maps[-1][-1] = INF
    
    bfs(maps)

    return -1 if maps[-1][-1] == INF else maps[-1][-1]