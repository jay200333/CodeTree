import sys
sys.setrecursionlimit(1000000)

n, m = map(int,input().split())
parent = [i for i in range(n+1)]
size = [1 for i in range(n+1)]

def find(cur):
    if cur == parent[cur]:
        return cur
    
    parentCur = find(parent[cur])
    parent[cur] = parentCur
    return parentCur

def union(a, b):
    parentA = find(a)
    parentB = find(b)
    if parentA == parentB:
        return
    if parentA <= parentB:
        parent[parentB] = parentA
        size[parentA] += size[parentB]
    else:
        parent[parentA] = parentB
        size[parentB] += size[parentA]


for _ in range(m):
    op = input().split()
    if op[0] == 'x':
        union(int(op[1]), int(op[2]))
    else:
        p = find(int(op[1]))
        print(size[p])
