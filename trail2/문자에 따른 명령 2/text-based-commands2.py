dirs = input()

# Please write your code here.
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
y, x = 0, 0

idx = 1
for i in dirs:
    if i == 'L':
        idx = (idx + 3) % 4
    elif i == 'R':
        idx = (idx + 1) % 4
    elif i == 'F':
        y += dir[idx][0]
        x += dir[idx][1]

print(x, y)    