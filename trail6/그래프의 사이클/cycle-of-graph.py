n, m = map(int, input().split())
parent = [i for i in range(n+1)]

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
        return False
    
    if parentA < parentB:
        parent[parentB] = parentA
    else:
        parent[parentA] = parentB
    return True

for i in range(1, m+1):
    s, e = map(int,input().split())
    if not union(s, e):
        print(i)
        break
else:
    print("happy")




