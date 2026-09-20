n, m = map(int, input().split())

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = 0

graph = [[''] * m for _ in range(n)]
x, y = 0, 0
graph[x][y] = 'A'
for i in range(1, n*m):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] != '':
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    x, y = nx, ny
    graph[x][y] = chr(65 + (i % 26))

for i in range(n):
    print(*graph[i])
