MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

# Please write your code here.
users.sort(key = lambda x: x[1])
print(f"{users[0][0]} {users[0][1]}")