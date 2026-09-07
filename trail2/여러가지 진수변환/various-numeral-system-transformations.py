N, B = map(int, input().split())

# Please write your code here.
answer = ""
while N > 0:
    answer += str(N % B)
    N //= B
print(answer[::-1])