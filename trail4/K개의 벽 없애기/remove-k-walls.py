from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n, k = map(int, input().split())
walls = []
grid = [list(map(int, input().split())) for _ in range(n)]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            walls.append((i,j))

answer = int(1e9)
visited_wall = [False] * len(walls)

def backtrack(count, cur):
    global answer
    if count == k:
        answer = min(answer, bfs())
        return
    
    for i in range(cur, len(walls)):
        wx, wy = walls[i]

        grid[wx][wy]= 0
        backtrack(count + 1, i + 1)
        grid[wx][wy] = 1

def bfs():
    visited = [[-1] * n for _ in range(n)]
    queue = deque([(r1, c1)])
    visited[r1][c1] = 0

    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if visited[nx][ny] == -1 and grid[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return int(1e9)

backtrack(0, 0)

if answer == int(1e9):
    answer = -1
print(answer)