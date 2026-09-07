n = int(input())

answer = ""
# Please write your code here.
if n == 0:
    answer = "0"
else:
    while n > 0:
        answer += str(n%2)
        n//=2
print(answer[::-1])