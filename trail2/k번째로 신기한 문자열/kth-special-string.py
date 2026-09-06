n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
filtered_str = [i for i in str if i.startswith(t)]
filtered_str.sort()
print(filtered_str[k-1])