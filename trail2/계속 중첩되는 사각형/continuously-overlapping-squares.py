n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
result = [[0] * 201 for _ in range(201)]
for i in range(n):
    for x in range(x1[i] + 100, x2[i] + 100):
        for y in range(y1[i] + 100, y2[i] + 100):
            if i % 2 == 0:
                result[x][y] = 1
            else:
                result[x][y] = 2

answer = 0
for i in range(201):
    answer += result[i].count(2)
print(answer)