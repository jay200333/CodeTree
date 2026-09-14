n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0

for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if grid[nx][ny] == 1:
                count += 1
        if count >= 3:
            answer += 1

print(answer)