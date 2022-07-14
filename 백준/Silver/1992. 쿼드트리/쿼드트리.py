import sys

input = sys.stdin.readline

def func(row, col, n):
    global result

    cur = tree[row][col]

    for i in range(row, row + n): # base statement : n == 1 이면 자동으로 1번 실행 후 종료.
        for j in range(col , col + n):
            if cur != tree[i][j]: # 유효성 검사 탈락시
                half = n // 2
                result.append("(")
                func(row, col, half) #순서 : 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 순
                func(row, col + half, half)
                func(row + half, col, half)
                func(row + half, col + half, half)
                result.append(")")
                return

    result.append(cur)

n = int(input().rstrip('\n'))

tree = [list(map(int, input().rstrip('\n'))) for _ in range(n)]

result = []

func(0, 0, n)
print(''.join(map(str, result)))