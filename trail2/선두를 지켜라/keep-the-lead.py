n, m = map(int, input().split())
distance_n = [0] * 1000001
distance_m = [0] * 1000001
# Process A's movements

cur_time = 1
for _ in range(n):
    vi, ti = map(int, input().split())
    for t in range(ti):
        distance_n[cur_time] = distance_n[cur_time-1] + vi
        cur_time += 1
        

# Process B's movements
cur_time = 1
for _ in range(m):
    vi, ti = map(int, input().split())
    for t in range(ti):
        distance_m[cur_time] = distance_m[cur_time-1] + vi
        cur_time += 1
    
answer = 0
leader = 0
# Please write your code here.
for i in range(1, cur_time):
    if distance_n[i] > distance_m[i]:
        if leader == 2:
            answer += 1
        leader = 1
    elif distance_n[i] < distance_m[i]:
        if leader == 1:
            answer += 1
        leader = 2
print(answer) 