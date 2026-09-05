N = int(input())

# Please write your code here.
def rec(i):
    if i == 1:
        return 1
    if i == 2:
        return 2
    return rec(i//3) + rec(i-1)

print(rec(N))