a, b = map(int, input().split())

# Please write your code here.
answer = 1
for i in range(b):
    answer *= a
print(answer)