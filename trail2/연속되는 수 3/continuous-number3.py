N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
answer, count = 0, 0
for i in range(N):
    if i >= 1 and (arr[i] * arr[i-1] > 0):
        count += 1
    else:
        count = 1 
    answer = max(count, answer)

print(answer)