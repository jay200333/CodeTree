N, M = map(int, input().split())
arr = [input() for _ in range(N)]

answer = 0

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            for k in range(8):
                nx1, ny1 = i + dx[k] * 2, j + dy[k] * 2
                if nx1 < 0 or ny1 < 0 or nx1 >= N or ny1 >= M: continue
                nx2, ny2 = i + dx[k], j + dy[k]
                if arr[nx1][ny1] == 'E' and arr[nx2][ny2] == 'E':
                    answer += 1

print(answer)