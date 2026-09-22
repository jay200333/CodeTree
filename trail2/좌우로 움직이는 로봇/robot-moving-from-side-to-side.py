n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

distanceA = [0] * 2000001
disA = 0
timeA = 1
for i in range(n):
    time, dir = t[i], d[i]
    if dir == 'L':
        for _ in range(time):
            disA -= 1
            distanceA[timeA] = disA
            timeA += 1
            
    elif dir == 'R':
        for _ in range(time):
            disA += 1
            distanceA[timeA] = disA
            timeA += 1
            

distanceB = [0] * 2000001
disB = 0
timeB = 1
for i in range(m):
    time, dir = t_b[i], d_b[i]
    if dir == 'L':
        for _ in range(time):
            disB -= 1
            distanceB[timeB] = disB
            timeB += 1
            
    elif dir == 'R':
        for _ in range(time):
            disB += 1
            distanceB[timeB] = disB
            timeB += 1
            
maxTime = max(timeA, timeB)
for i in range(timeA, maxTime):
    distanceA[i] = disA

for i in range(timeB, maxTime):
    distanceB[i] = disB

answer = 0

for i in range(1, maxTime):
    if distanceA[i-1] != distanceB[i-1] and distanceA[i] == distanceB[i]:
        answer += 1
print(answer)
