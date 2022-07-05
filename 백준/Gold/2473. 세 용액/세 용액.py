from sys import stdin
input = stdin.readline

def solve(arr):
    
    ret_val = [0, 1, 2]
    min_val = float('inf')
    for i in range(len(arr) - 2):
        base = arr[i]
        left, right = i + 1, len(arr) - 1
        while left < right:
            val = base + arr[left] + arr[right]
            if abs(val) < min_val:
                min_val = abs(val)
                ret_val[0], ret_val[1], ret_val[2] = base, arr[left], arr[right]
                if min_val == 0:
                    return ret_val
            elif val < 0:
                left += 1
            else:
                right -= 1

    return ret_val

input()
arr = sorted(list(map(int, input().split())))
print(*solve(arr))