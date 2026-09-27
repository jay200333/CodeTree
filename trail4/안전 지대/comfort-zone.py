import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_height = 0
for i in range(n):
    max_height = max(max_height, max(grid[i]))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = [1, 0]

def dfs(r, c, h):
    for i in range(4):
        nx = dx[i] + r
        ny = dy[i] + c
        if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
        if grid[nx][ny] > h and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, h)

for height in range(1, max_height + 1):
    count = 0
    visited = [[False] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if grid[x][y] > height and not visited[x][y]:
                count += 1
                visited[x][y] = True
                dfs(x, y, height)
    if count > answer[1]:
        answer[0] = height
        answer[1] = count

print(*answer)