n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
arr = []
answer = 0

def calculate():
    value = int(1e9)
    for i in range(n):
        value = min(value, grid[i][arr[i]])
    return value

def backtrack(cur):
    global answer
    if cur == n:
        result = calculate()
        answer = max(answer, result)
        return

    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        arr.append(i)
        backtrack(cur + 1)
        arr.pop()
        visited[i] = False

backtrack(0)
print(answer)
