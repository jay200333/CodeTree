n = int(input())
grid = [[0] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = n//2, n//2
dir, moveCount = 0, 1
number = 1

while number <= n*n:
    for _ in range(moveCount):
        grid[x][y] = number
        number += 1
        x = x + dx[dir]
        y = y + dy[dir]
        if x < 0 or y <0 or x >= n or y >= n:
            break
    
    dir = (dir + 1) % 4
    if dir == 0 or dir == 2:
        moveCount += 1

for i in range(n):
    print(*grid[i])
