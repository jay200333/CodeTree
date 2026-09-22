R, C = map(int, input().split())
graph = [list(input().split()) for _ in range(R)]

answer = 0
for i in range(1, R):
    for j in range(1, C):
        flag = False
        if graph[i][j] != graph[0][0]:
            flag = True
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                if flag and graph[i][j] != graph[k][l] and graph[k][l] != graph[R-1][C-1]:
                    answer += 1

print(answer)