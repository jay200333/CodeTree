import sys
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = [0, 0]
visited = [[False] * n for _ in range(n)]
count = 0

def dfs(r,c,h):
    global count
    for i in range(4):
        nx = dx[i] + r
        ny = dy[i] + c
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        if grid[nx][ny] == h and not visited[nx][ny]:
            visited[nx][ny] = True
            count += 1
            dfs(nx, ny, h)

for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            visited[x][y] = True
            count = 1
            dfs(x, y, grid[x][y])
            if count >= 4:
                answer[0] += 1
            if answer[1] < count:
                answer[1] = count

print(*answer)
