n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
numbers = l + r + d
for i in range(t):
    temp = numbers[3*n-1]
    for j in range(3*n-1, 0, -1):
        numbers[j] = numbers[j-1]
    numbers[0] = temp

print(*numbers[:n])
print(*numbers[n:2*n])
print(*numbers[2*n:])