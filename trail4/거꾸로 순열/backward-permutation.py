n = int(input())
result = []
visited = [False] * (n+1)

def backtrack(cur):
    if cur == 0:
        print(*result)
        return

    for i in range(n, 0, -1):
        if visited[i]: continue
        visited[i] = True
        result.append(i)
        backtrack(cur-1)
        result.pop()
        visited[i] = False

backtrack(n)
