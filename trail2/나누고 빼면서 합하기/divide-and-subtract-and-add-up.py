n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

# Please write your code here.
answer = 0
while m >= 1:
    answer += A[m]
    if m % 2 == 0:
        m //= 2
    else:
        m -= 1
print(answer)