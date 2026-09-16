commands = input()

# Please write your code here.
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
x, y = 0, 0

answer = 0
dir = 1

for c in commands:
    if c == 'L':
        dir = (dir - 1) % 4
    elif c == 'R':
        dir = (dir + 1) % 4
    elif c == 'F':
        x += dx[dir]
        y += dy[dir]
    answer += 1
    if x == 0 and y == 0:
        print(answer)
        break
else:
    print(-1)

