from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

visited = [[-1] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            queue.append((i,j))
            visited[i][j] = 0

# Please write your code here.
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        if visited[nx][ny] == -1 and grid[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == -1:
            visited[i][j] = -2

for i in range(n):
    print(*visited[i])
