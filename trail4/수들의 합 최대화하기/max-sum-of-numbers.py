n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = 0
arr = []

def calculate():
    temp = 0
    for i in range(n):
        temp += grid[i][arr[i]]
    return temp

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
