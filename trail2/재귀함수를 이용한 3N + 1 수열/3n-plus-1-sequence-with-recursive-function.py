n = int(input())

# Please write your code here.
def rec(i):
    if i == 1:
        return 0
    if i % 2 == 0:
        return rec(i//2) + 1
    else:
        return rec(i * 3 + 1) + 1

print(rec(n))
