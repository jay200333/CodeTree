n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
answer, count = 0, 0
for i in range(n):
    if arr[i] > t:
        count += 1
    else:
        count = 0
    answer = max(answer, count)
print(answer)