N = int(input())

# Please write your code here.
def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n-1)

print(sum_rec(N))
