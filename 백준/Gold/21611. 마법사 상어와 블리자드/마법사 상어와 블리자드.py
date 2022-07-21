import sys

input = sys.stdin.readline

nm = 51 # n<=49 2칸정도 여유롭게 메모리 지정.

n, m = map(int, input().rstrip('\n').split())
data = [[0] * nm for _ in range(nm)]        
num = [[0] * nm for _ in range(nm)] # 각 칸의 번호를 부여하기 위한 배열
a = [0] * (nm*nm) # 일렬로 폈을 때의 구슬 번호 배열
b = [0] * (nm*nm) # 일렬로 폈을 때의 구슬 번호 배열
cnt = [0] * 5 

# 나선형 numbering : 바깥쪽에서 안쪽으로
def calculate_snail_num():
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동, 남, 서, 북
    x, y = 1, 1
    d = 0
    v = n * n - 1
    
    while v != 0:
        a[v] = data[x][y]
        num[x][y] = v
        v -= 1
        
        while True:
            nx = x + dir[d][0]
            ny = y + dir[d][1]

            # num[nx][ny]가 0이 아니다 = 이미 넘버링 된 곳을 또 방문하였다는 의미
            if ((nx < 1 or ny < 1 or nx > n or ny > n) or num[nx][ny] != 0):
                d = (d+1) % 4
                continue
                
            x = nx
            y = ny # 좌표 갱신
            break

# 얼음 파편을 던진다.
def blizzard(d, s):
    dir = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    x = n//2 + 1 
    y = n//2 + 1 
    for i in range(1, s+1):
        x += dir[d][0]
        y += dir[d][1]
        a[num[x][y]] = 0

    compress()

# 빈 칸 없이 압축하는 함수
def compress():
    last = 0 # 마지막으로 값이 교환되어 들어간 위치
    for i in range(1, n*n):
        if a[i] == 0:
            continue
        
        last += 1
        a[last] = a[i]

    for i in range(last+1, n*n):
        a[i] = 0

# 1번 폭발하는 함수
def bomb():
    flag = False

    i = 1

    while i <= n*n-1 and a[i] != 0:
        j = i 
        
        # i번 칸부터 j번 칸까지 연속한 구슬을 찾을 것!
        while (j+1 <= (n*n-1) and a[i] == a[j + 1]):
            j += 1

        #만일 연속한 구슬이 4개 이상이라면?
        if (j - i + 1 >= 4):
            cnt[a[i]] += (j - i + 1)
            for k in range(i, j+1):
                a[k] = 0
            flag = True
        i = j
        i += 1

    return flag

def convert():
    A, B = 0, 0
    last = 0
    i = 1

    for idx in range(1, n*n):
        b[idx] = 0

    # i번 칸부터 연속된 구슬을 찾을 것.
    while i <= n*n-1 and a[i] != 0:
        j = i 
        
        while (j+1 <= n*n-1 and a[i] == a[j+1]):
            j += 1
        
        A = j - i + 1  # 구슬의 개수
        B = a[i] # 구슬의 번호

        if last < n*n-1:
            last += 1 
            b[last] = A
        if last < n*n-1:
            last += 1 
            b[last] = B

        i = j
        i += 1

    for k in range(1, n*n):
        a[k] = b[k]

def init():
    for i in range(1, n+1):
        line = [0] + list(map(int, input().rstrip('\n').split()))
        for j in range(1, n+1):
            data[i][j] = line[j]

def solve():
    calculate_snail_num()
    for _ in range(m):  
        # 3 . 얼음 던지기
        d, s = map(int, input().rstrip('\n').split())
        blizzard(d, s)

        # 4. 연쇄 폭발
        while bomb():
            compress()

        # 5. 그룹 변환
        convert()

    res = 0
    for i in range(1, 4):
        res += i * cnt[i]

    print(res)

init()
solve()