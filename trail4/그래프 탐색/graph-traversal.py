n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for i in range(m):
    s, e = edges[i]
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n+1)
answer = 0

def dfs(v):
    global answer
    visited[v] = True
    answer += 1
    for next in graph[v]:
        if visited[next]: continue
        dfs(next)

dfs(1)
print(answer - 1)
