n = int(input())
num = list(map(int, input().split()))

visited = [False] * n
answer = int(1e9)


def backtrack(cur, count):
    global answer
    if cur == n-1:
        answer = min(answer, count)
        return
    
    curNum = num[cur]
    for i in range(1, curNum+1):
        nx = cur + i
        if nx < 0 or nx >= n: continue
        visited[nx] = True
        backtrack(nx, count + 1)
        visited[nx] = False

backtrack(0, 0)
if answer == int(1e9):
    answer = -1
print(answer)
