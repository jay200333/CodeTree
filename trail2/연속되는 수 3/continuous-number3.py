N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
answer = 1
for i in range(N):
    if i == 0 or ( arr[i] < 0 and arr[i-1] > 0) or ( arr[i] > 0 and arr[i-1] < 0):
        count = 1
    else:
        count += 1 
        answer = max(count, answer)

print(answer)