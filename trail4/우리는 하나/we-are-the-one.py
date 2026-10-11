from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
arr = []

def calculate():
    q = deque(arr)
    visited = [[False] * n for _ in range(n)]
    for x, y in arr:
        visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if not visited[nx][ny] and abs(grid[nx][ny] - grid[x][y]) in list(range(u, d+1)):
                q.append((nx, ny))
                visited[nx][ny] = True
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                count += 1
    return count

def backtrack(cur, r, c):
    global answer
    if cur == k:
        result = calculate()
        answer = max(answer, result)
        return
    
    for i in range(r, n):
        for j in range(c, n):
            if (i, j) not in arr:
                arr.append((i, j))
                backtrack(cur + 1, i, j)
                arr.pop()

backtrack(0, 0, 0)
print(answer)
