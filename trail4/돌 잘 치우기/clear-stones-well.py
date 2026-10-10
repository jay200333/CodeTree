from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, k, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
rocks = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            rocks.append((i, j))

answer = 0
startPoint = []
for _ in range(k):
    x, y = map(int, input().split())
    startPoint.append((x-1, y-1))

def bfs():
    visited = [[False] * n for _ in range(n)]
    count = k
    for x, y in startPoint:
        visited[x][y] = True
    q = deque(startPoint)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if not visited[nx][ny] and graph[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count

def backtrack(idx, cur):
    global answer

    if cur == m:
        result = bfs()
        answer = max(answer, result)
        return
    
    for i in range(idx, len(rocks)):
        rx, ry = rocks[i]
        graph[rx][ry] = 0
        backtrack(i + 1, cur + 1)
        graph[rx][ry] = 1

backtrack(0, 0)
print(answer)