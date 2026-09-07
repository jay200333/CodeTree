from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
person = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            person.append((i,j))

# Please write your code here.
def bfs(x,y):
    queue = deque([(x,y)])
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 3:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if visited[nx][ny] == 0 and grid[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    else:
        return -1

answer = [[0] * n for _ in range(n)]    
for i,j in person:
    result = bfs(i,j)
    answer[i][j] = result - 1 if result != - 1 else -1

for i in range(n):
    print(*answer[i])