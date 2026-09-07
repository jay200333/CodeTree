from collections import deque

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0] * (n+1) for _ in range(n+1)]

# Please write your code here.
queue = deque([(r1, c1)])
visited[r1][c1] = 1

while queue:
    curX, curY = queue.popleft()
    if curX == r2 and curY == c2:
        print(visited[curX][curY] - 1)
        break
    for i in range(8):
        nx = dx[i] + curX
        ny = dy[i] + curY
        if nx < 1 or ny < 1 or nx > n or ny > n: continue
        if visited[nx][ny] == 0:
            visited[nx][ny] = visited[curX][curY] + 1
            queue.append((nx,ny))
else:
    print(-1)