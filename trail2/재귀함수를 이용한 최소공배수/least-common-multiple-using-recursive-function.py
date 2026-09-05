n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a,b):
    return a * b // gcd(a,b)

def rec(i):
    if i == 0:
        return arr[i]
    return lcm(rec(i-1), arr[i])

print(rec(n-1))