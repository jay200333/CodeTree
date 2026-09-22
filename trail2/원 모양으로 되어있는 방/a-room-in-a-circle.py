n = int(input())
a = [int(input()) for _ in range(n)]
answer = int(1e9)

for i in range(n):
    result = 0
    for j in range(i, i+n):
        if i == j: continue
        result += a[j % n] * abs(j - i)
    answer = min(result, answer)

print(answer)