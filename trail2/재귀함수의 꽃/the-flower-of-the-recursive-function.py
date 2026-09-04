N = int(input())

# Please write your code here.
def f(a, t, l):
    if t >= l:
        return
    print(a[t], end=' ')
    f(a, t + 1, l)
    print(a[t], end=' ')

a = [i for i in range(N, 0, -1)]
f(a, 0, N)