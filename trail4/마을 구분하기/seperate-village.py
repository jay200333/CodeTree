n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
village = []
visited = [[False] * n for _ in range(n)]
count = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(r,c):
    global count

    for i in range(4):
        nx = dx[i] + r
        ny = dy[i] + c
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        if grid[nx][ny] == 1 and not visited[nx][ny]:
            count += 1
            visited[nx][ny] = True
            dfs(nx, ny)

for x in range(n):
    for y in range(n):
        if grid[x][y] == 1 and not visited[x][y]:
            visited[x][y] = True
            count = 1
            dfs(x, y)
            village.append(count)

print(len(village))
village.sort()
for c in village:
    print(c)
