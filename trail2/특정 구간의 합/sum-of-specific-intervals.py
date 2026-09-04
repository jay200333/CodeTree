n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for i in range(m):
    s, e = queries[i]

    print(sum(arr[s-1: e]))