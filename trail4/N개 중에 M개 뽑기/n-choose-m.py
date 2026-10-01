N, M = map(int, input().split())

visited = [False] * (N + 1)
result = []

def backtrack(idx, cur):
    if cur == M:
        print(*result)
        return
    
    for i in range(idx, N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtrack(i, cur + 1)
            result.pop()
            visited[i] = False

backtrack(1, 0)
