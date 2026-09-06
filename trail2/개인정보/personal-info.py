n = 5
info = []

for _ in range(n):
    n, h, w = input().split()
    info.append((n, int(h), float(w)))

# Please write your code here.
info.sort(key = lambda x: x[0])
print("name")
for i in info:
    print(*i)

info.sort(key = lambda x: -x[1])
print()
print("height")
for i in info:
    print(*i)