from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# Please write your code here.
queue = deque([(0,0)])
visited[0][0] = 1
while queue:
    curX, curY = queue.popleft()
    if curX == n-1 and curY == m-1:
        print(visited[curX][curY]- 1)
        break
    for i in range(4):
        nx = dx[i] + curX
        ny = dy[i] + curY
        if nx < 0 or ny < 0 or nx >= n or ny>= m: continue
        if visited[nx][ny] == 0 and a[nx][ny] == 1:
            visited[nx][ny] = visited[curX][curY] + 1
            queue.append((nx,ny))
else:
    print(-1)
