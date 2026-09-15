n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r) - 1, int(c) - 1

# Please write your code here.
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

if d == 'L':
    dir = 0
elif d == 'U':
    dir = 1
elif d == 'D':
    dir = 2
elif d == 'R':
    dir = 3

for i in range(t):
    nx = r + dx[dir]
    ny = c + dy[dir]

    if nx >= 0 and nx < n and ny >= 0 and ny < n:
        r = nx
        c = ny
    else:
        dir = 3 - dir
print(r+1, c+1)


