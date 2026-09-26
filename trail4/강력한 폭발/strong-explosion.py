bombType = [
    [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)],
    [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
    ]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
result = []
bomb = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb.append((i,j))
answer = 0

def calculate():
    bombArea = [[False] * n for _ in range(n)]
    for i in range(len(result)):
        curType = result[i]
        bombPosY, bombPosX = bomb[i]
        for dy, dx in bombType[curType]:
            ny = bombPosY + dy
            nx = bombPosX + dx
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            bombArea[ny][nx] = True
    
    bombCount = 0
    for i in range(n):
        for j in range(n):
            if bombArea[i][j]:
                bombCount += 1
    return bombCount

def backtrack(cur):
    global answer
    if cur == len(bomb):
        area = calculate()
        answer = max(answer, area)
        return
    
    for i in range(3):
        result.append(i)
        backtrack(cur + 1)
        result.pop()

backtrack(0)
print(answer)
