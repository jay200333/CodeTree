n = int(input())
x = []
dir = []
temp = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
visited = [0] * 2001
cur_idx = 0
for i in range(n):
    if dir[i] == 'R':
        left = cur_idx
        right = cur_idx + x[i]
        cur_idx += x[i]
    else:
        left = cur_idx - x[i]
        right = cur_idx
        cur_idx -= x[i]
    temp.append((left, right))

for left, right in temp:
    for j in range(left, right):
        visited[j+1000] += 1
        
answer = 0
for i in visited:
    if i >= 2:
        answer += 1
print(answer)