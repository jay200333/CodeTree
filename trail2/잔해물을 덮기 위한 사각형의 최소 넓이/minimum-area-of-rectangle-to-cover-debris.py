rects = [tuple(map(int, input().split() )) for _ in range(2)]

# Please write your code here.
result = [[0] * 2001 for _ in range(2001)]
for i, (x1, y1, x2, y2) in enumerate(rects, start = 1):
    x1, y1 = x1 + 1000, y1 + 1000
    x2, y2 = x2 + 1000, y2 + 1000
    for x in range(x1, x2):
        for y in range(y1, y2):
            result[x][y] = i

answer = 0
minX, minY = 2001, 2001
maxX, maxY = 0, 0
isRect1 = False
for x in range(2001):
    for y in range(2001):
        if result[x][y] == 1:
            isRect1 = True
            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, x)
            maxY = max(maxY, y)

if isRect1:
    print((maxX - minX + 1) * (maxY - minY + 1))
else:
    print(0)
