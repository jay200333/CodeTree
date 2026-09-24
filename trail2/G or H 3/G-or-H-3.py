n, k = map(int, input().split())
x = []
c = []
arr = [0] * 10001
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)
    arr[int(pos)] = 1 if char == 'G' else 2

answer = 0
for i in range(10000-k+1):
    result = sum(arr[i:i+k+1])
    answer = max(answer, result)

print(answer)