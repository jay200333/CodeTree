n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
result = [[0] * 201 for _ in range(201)]
for i in range(n):
    for j in range(x[i], x[i] + 8):
        for k in range(y[i], y[i] + 8):
            result[j][k] = 1

answer = 0
for i in range(201):
    answer += sum(result[i])

print(answer)