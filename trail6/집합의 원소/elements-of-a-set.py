n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(cur):
    if cur == parent[cur]:
        return cur

    parentCur = find(parent[cur])
    parent[cur] = parentCur
    return parentCur

def union(first, second):
    firstP = find(first)
    secondP = find(second)
    if firstP <= secondP:
        parent[secondP] = firstP
    else:
        parent[firstP] = secondP

for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(a, b)
    elif t == 1:
        if find(a) == find(b):
            print(1)
        else:
            print(0)
