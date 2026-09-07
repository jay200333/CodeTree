n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [0] * 101
for s, e in segments:
    for j in range(s, e+1):
        visited[j] += 1
print(max(visited))