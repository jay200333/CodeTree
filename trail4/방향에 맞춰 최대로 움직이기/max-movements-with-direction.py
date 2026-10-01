n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
visited = [[False] * n for _ in range(n)]

def backtrack(r,c,count):
    result = count
    dir = move_dir[r][c] - 1

    nx = r + dx[dir]
    ny = c + dy[dir]
    
    while 0 <= nx < n and 0 <= ny < n:
        if visited[nx][ny] == False and num[nx][ny] > num[r][c]:
            visited[nx][ny] = True
            result = max(result, backtrack(nx,ny,count+1))
            visited[nx][ny] = False

        nx += dx[dir]
        ny += dy[dir]
    return result

visited[r-1][c-1] = True
print(backtrack(r-1,c-1,0))
