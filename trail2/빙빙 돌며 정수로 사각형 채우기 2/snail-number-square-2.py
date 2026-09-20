n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dir = 0
x,y = 0,0
graph = [[0] * m for _ in range(n)]
graph[x][y] = 1
for i in range(2, n*m+1):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] != 0:
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    x, y = nx, ny
    graph[x][y] = i

for i in range(n):
    print(*graph[i])

