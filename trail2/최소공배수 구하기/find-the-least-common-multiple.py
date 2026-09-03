n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n%m)

print(n*m//gcd(n,m))