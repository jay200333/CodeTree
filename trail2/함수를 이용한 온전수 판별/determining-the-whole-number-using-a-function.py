a, b = map(int, input().split())

# Please write your code here.
def isonjeon(n):
    if n % 2 != 0 and n%10 != 5 and not(n%3 == 0 and n%9!=0):
        return True
    return False

answer = 0
for i in range(a, b+1):
    if isonjeon(i):
        answer += 1
print(answer)
