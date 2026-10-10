from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque([(0, 0)])
visited[0][0] = True

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
        if not visited[nx][ny] and a[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))

if visited[-1][-1]:
    print(1)
else:
    print(0)
