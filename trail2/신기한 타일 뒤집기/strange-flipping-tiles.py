n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
result = [0] * 200001
cur_idx = 100000

for i in range(n):
    if dir[i] == 'L':
        left = cur_idx - x[i] + 1
        right = cur_idx
        cur_idx = left

        for j in range(left, right + 1):
            result[j] = 1
    else:
        left = cur_idx
        right = cur_idx + x[i] - 1
        cur_idx = right

        for j in range(left, right + 1):
            result[j] = 2

white_count = 0
black_count = 0

for i in result:
    if i == 1:
        white_count += 1
    elif i == 2:
        black_count += 1

print(white_count, black_count)