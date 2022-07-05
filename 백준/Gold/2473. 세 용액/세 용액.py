import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))
solutions = list(map(int, input().rstrip('\n').split()))
solutions.sort()

def solve(solutions):
    tmp = sys.maxsize
    min_value = sys.maxsize
    result = []

    for i in range(len(solutions) - 2):
        if i > 0 and solutions[i] == solutions[i - 1]:
            continue
        
        left, right = i + 1, len(solutions) - 1
        while left < right:
            tmp = solutions[i] + solutions[left] + solutions[right]
            
            if abs(tmp) < abs(min_value):
                result = [solutions[i], solutions[left], solutions[right]]
                min_value = tmp

            if tmp < 0:
                left += 1
            
            elif tmp > 0:
                right -= 1

            # tmp == 0
            else:
                result = [solutions[i], solutions[left], solutions[right]]
                return result

    return result

result = solve(solutions)
print(*result)