from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0
visited = [[False] * n for _ in range(n)]
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for _ in range(k):
    a, b = map(int, input().split())
    q.append((a-1, b-1))
    visited[a-1][b-1] = True
    answer += 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        if not visited[nx][ny] and grid[nx][ny] == 0:
            q.append((nx, ny))
            visited[nx][ny] = True
            answer += 1

print(answer)