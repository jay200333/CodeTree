n = int(input())
info = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    info.append((n_i, h_i, w_i))

# Please write your code here.
info.sort(key=lambda x: x[1])
for i in info:
    print(i[0], i[1], i[2])