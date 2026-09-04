a, b = map(int, input().split())

# Please write your code here.
def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def isEven(n):
    if sum(list(map(int,str(n)))) % 2 == 0:
        return True
    return False

answer = 0

for i in range(a, b+1):
    if isPrime(i) and isEven(i):
        answer += 1
print(answer)