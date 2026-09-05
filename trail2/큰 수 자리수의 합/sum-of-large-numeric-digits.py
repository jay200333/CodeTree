a, b, c = map(int, input().split())

# Please write your code here.
def sum_rec(n):
    if n < 10:
        return n
    return sum_rec(n//10) + n % 10

print(sum_rec(a*b*c))