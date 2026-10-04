n = int(input())
parent = [i for i in range(n+1)]

def find(cur):
    if  parent[cur] == cur:
        return cur
    parentCur = find(parent[cur])
    parent[cur] = parentCur
    return parentCur

def union(a, b):
    parentA = find(a)
    parentB = find(b)

    if parentA == parentB:
        return

    if parentA < parentB:
        parent[parentB] = parentA
    else:
        parent[parentA] = parentB

for _ in range(n-2):
    a, b = map(int,input().split())
    union(a, b)

roots = set()
for i in range(1, n + 1):
  roots.add(find(i))

root_list = list(roots)

print(root_list[0], root_list[1])