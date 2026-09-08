n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
mine = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            mine.append((i,j))
answer = 0
for k in range(n+1):
    cost = k**2 + (k+1)**2
    for r in range(n):
        for c in range(n):
            count = sum(1 for hr, hc in mine if abs(r-hr) + abs(c-hc) <= k)
            if count * m >= cost:
                answer = max(answer, count)
print(answer)

