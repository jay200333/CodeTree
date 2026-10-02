n, m, k = map(int, input().split())

def find(cur):
    if cur == parent[cur]:
        return cur
    parentCur = find(parent[cur])
    parent[cur] = parentCur
    return parentCur

def union(a, b):
    parentA = find(a)
    parentB = find(b)
    if parentA <= parentB:
        parent[parentB] = parentA
    else:
        parent[parentA] = parentB

parent = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
test = list(map(int,input().split()))

flag = False
first = test[0]
for i in range(1, k):
    if find(first) != find(test[i]):
        flag = True
        break

if flag:
    print(0)
else:
    print(1)
