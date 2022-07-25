answer = 0 

def dfs(idx, tmp, numbers, target):
    global answer
    
    # base statement
    if len(numbers) == idx:
        if tmp == target: # 목표 값에 도달한 경우.
            answer += 1
            return
        
        return
    
    dfs(idx + 1, tmp + numbers[idx], numbers, target)
    dfs(idx + 1, tmp - numbers[idx], numbers, target)    
    
def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    
    return answer