n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
offset = 100

result = [[0] * 201 for _ in range(201)]
for i in range(n):
    x11, x22, y12, y22 = x1[i], x2[i], y1[i], y2[i]
    for j in range(x11, x22):
        for k in range(y12, y22):
            result[j][k] = 1

answer = 0
for i in range(201):
    answer += sum(result[i])
print(answer)