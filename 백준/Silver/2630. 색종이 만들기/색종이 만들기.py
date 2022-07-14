import sys

input = sys.stdin.readline

def func(row, col, n):
	global white, blue
	curr = paper[row][col]
	for i in range(row, row + n):
		for j in range(col, col + n):
			if curr != paper[i][j]:
				half = n // 2
				func(row, col, half)
				func(row, col+half, half)
				func(row+half, col, half)
				func(row+half, col+half, half)
				return

	if paper[row][col] == 1:
		blue += 1

	elif paper[row][col] == 0:
		white += 1

n = int(input().rstrip('\n'))

paper = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

white, blue = 0, 0

func(0, 0, n)
print(white)
print(blue)