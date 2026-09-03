a, b = input().split()
b_list = list(b)
b_list[:2] = list(a)[:2]
print("".join(b_list))