dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dir = 1
x, y = N//2, N//2
answer = board[x][y]

for i in range(T):
    if str[i] == 'L':
        dir = (dir - 1) % 4
    elif str[i] == 'R':
        dir = (dir + 1) % 4
    elif str[i] == 'F':
        nx = dx[dir] + x
        ny = dy[dir] + y
        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        x, y = nx, ny
        answer += board[x][y]
print(answer)