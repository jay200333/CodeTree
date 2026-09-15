n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = 0
# Please write your code here.

x, y = 0, 0
arr[x][y] = 1
nx, ny = 0, 0

for i in range(2, n * m + 1):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] != 0:
        dir = (dir + 1) % 4
    
    x, y = x + dx[dir], y + dy[dir]
    arr[x][y] = i


for j in range(n):
    print(*arr[j])
