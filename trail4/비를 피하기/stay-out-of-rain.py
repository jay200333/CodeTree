from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
shelter = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            shelter.append((i,j))
            visited[i][j] = 0

# Please write your code here.
def bfs():
    queue = deque(shelter)
        
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if visited[nx][ny] == -1 and grid[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

bfs()
answer = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            answer[i][j] = visited[i][j]

for row in answer:    
    print(*row)