n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
# '\'
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir = 0
if k in range(1, n + 1):
    x, y = 0, k - 1
    dir = 0
elif k in range(n + 1, n * 2 + 1):
    x, y = k - n - 1, n - 1
    dir = 1
elif k in range(n * 2 + 1, n * 3 + 1):
    x, y = n - 1, 3 * n - k
    dir = 2
else:
    x, y = 4 * n - k, 0
    dir = 3

answer = 0
def inRange(r, c):
    if r < 0 or c < 0 or r >= n or c >= n:
        return False
    return True

while inRange(x, y):
    if grid[x][y] == '\\':
        if dir == 0: dir = 3
        elif dir == 3: dir = 0
        elif dir == 1: dir = 2
        elif dir == 2: dir = 1
    elif grid[x][y] == '/':
        if dir == 0: dir = 1
        elif dir == 1: dir = 0
        elif dir == 2: dir = 3
        elif dir == 3: dir = 2
    x += dx[dir]
    y += dy[dir]
    answer += 1
print(answer)