n = int(input())
visited = [False] * (n+1)
result = []

def backtrack(cur):
    if cur == n:
        print(*result)
        return
    
    for i in range(1, n+1):
        if visited[i]: continue
        visited[i] = True
        result.append(i)
        backtrack(cur + 1)
        result.pop()
        visited[i] = False

backtrack(0)
