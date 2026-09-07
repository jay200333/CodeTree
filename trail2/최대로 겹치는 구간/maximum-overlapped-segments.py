n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
blocks = [0] * 201

for s, e in segments:
    for j in range(s, e):
        blocks[j + 100] += 1
print(max(blocks))
