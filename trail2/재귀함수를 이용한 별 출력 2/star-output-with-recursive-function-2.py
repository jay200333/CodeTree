n = int(input())

# Please write your code here.
def f(a, t, l):
    if t >= l:
        return
    print("* " * a[t])
    f(a, t + 1, l)
    print("* " * a[t])

a = [i for i in range(n, 0, -1)]
f(a, 0, n)