N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

totalTime = sum(t)
distanceA = [0] * (totalTime + 1)
distanceB = [0] * (totalTime + 1)

curTimeA = 1
for i in range(N):
    vi, ti = v[i], t[i]
    for j in range(ti):
        distanceA[curTimeA] = distanceA[curTimeA - 1] + vi
        curTimeA += 1

curTimeB = 1
for i in range(M):
    vi, ti = v2[i], t2[i]
    for j in range(ti):
        distanceB[curTimeB] = distanceB[curTimeB - 1] + vi
        curTimeB += 1 

answer = 0
leader = 0
for i in range(1, totalTime + 1):
    if distanceA[i] > distanceB[i]:
        if leader != 1:
            answer += 1
        leader = 1
    elif distanceA[i] < distanceB[i]:
        if leader != 2:
            answer += 1
        leader = 2
    else:
        if leader != 3:
            answer += 1
        leader = 3

print(answer)
    