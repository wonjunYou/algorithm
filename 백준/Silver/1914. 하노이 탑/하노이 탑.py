import sys

input = sys.stdin.readline

def hanoi(start, end, n):
    
    if n == 1:
        print(start, end)
        return

    hanoi(start, 6-start-end, n-1) # n-1개를 중간 막대로 옮기고
    print(start, end) # n번째 블록을 최종 목적지로 옮기고
    hanoi(6-start-end, end, n-1) # n-1개의 블록을 최종 목적지로 옮긴다.


n = int(input().rstrip('\n'))

print(str(2**n - 1))

if n <= 20:
    hanoi(1, 3, n)