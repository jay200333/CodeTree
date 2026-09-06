n = int(input())
info = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    info.append((name_value, address_value, region_value))

# Please write your code here.
info.sort(key=lambda x: x[0], reverse = True)

print(f"name {info[0][0]}")
print(f"addr {info[0][1]}")
print(f"city {info[0][2]}")