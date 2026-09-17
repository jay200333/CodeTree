n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parents = [0] * (n+1)

for i in range(n-1):
    s, e = edges[i]
    graph[s].append(e)
    graph[e].append(s)

def dfs(s):
    for e in graph[s]:
        if not visited[e]:
            parents[e] = s
            visited[e] = True
            dfs(e)

visited[1] = True
dfs(1)
for i in range(2, n+1):
    print(parents[i])