n, m = map(int, input().split())

a = [0] * 1000001
time_a = 1
for i in range(n):
    direction, time = input().split()
    for j in range(int(time)):
        a[time_a] = a[time_a - 1] + (1 if direction == 'R' else -1)
        time_a += 1
    
    
b = [0] * 1000001
time_b = 1
for i in range(m):
    direction, time = input().split()
    for j in range(int(time)):
        b[time_b] = b[time_b - 1] + (1 if direction == 'R' else -1)
        time_b += 1

answer = -1
for i in range(1, time_a):
    if a[i] == b[i]:
        answer = i
        break

print(answer)
