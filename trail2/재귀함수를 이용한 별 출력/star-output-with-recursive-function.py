n = int(input())

# Please write your code here.
def rec(i):
    if i == n+1:
        return
    print("*" * i)
    rec(i+1)
rec(1)