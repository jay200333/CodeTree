n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

visited = [[False] * m for _ in range(n)]

def dfs(r,c):
    visited[r][c] = True
    for i in range(2):
        nx = dx[i] + r
        ny = dy[i] + c
        if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
        if grid[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)

visited[0][0] = True
dfs(0,0)

answer = 1 if visited[n-1][m-1] else 0
print(answer)