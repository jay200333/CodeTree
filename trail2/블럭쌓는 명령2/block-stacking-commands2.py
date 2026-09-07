n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
blocks = [0] * (n+1)

for s, e in commands:
    for j in range(s, e+1):
        blocks[j] += 1
print(max(blocks))