import sys
sys.setrecursionlimit(10**5)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    s, e, v = edges[i]
    graph[s].append((e, v))
    graph[e].append((s, v))

# Please write your code here.


def dfs(s, value):
    visited[s] = True
    max_node = s
    temp = value
    for next, next_value in graph[s]:
        if not visited[next]:
            far_node, far_value = dfs(next, value + next_value)
            if far_value > temp:
                temp = far_value
                max_node = far_node
    return max_node, temp

visited = [False] * (n+1)
far_node, far_value = dfs(1, 0)
visited = [False] * (n+1)
second_far_node, answer = dfs(far_node, 0)
print(answer)