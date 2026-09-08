n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
numbers = u + d
for i in range(t):
    temp = numbers[n*2-1]
    for j in range(n*2-1, 0, -1):
        numbers[j] = numbers[j-1]
    numbers[0] = temp

print(*numbers[:n])
print(*numbers[n:])