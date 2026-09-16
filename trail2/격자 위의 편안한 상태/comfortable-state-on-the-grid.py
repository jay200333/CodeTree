n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[0] * (n+1) for _ in range(n+1)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def check(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or nx > n or ny < 1 or ny > n: continue
        if graph[nx][ny]:
            count += 1
    if count == 3:
        return 1
    else:
        return 0

for i in range(m):
    r, c = points[i]
    graph[r][c] = 1
    print(check(r, c))