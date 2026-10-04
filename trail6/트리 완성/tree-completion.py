n, m = map(int, input().split())
parent = [i for i in range(n+1)]
answer = 0

def union(a, b):
    global answer
    parentA = find(a)
    parentB = find(b)

    if parentA == parentB:
        return False

    if parentA < parentB:
        parent[parentB] = parentA
    else:
        parent[parentA] = parentB
    return True

def find(cur):
    if cur == parent[cur]:
        return cur
    
    parentCur = find(parent[cur])
    parent[cur] = parentCur
    return parentCur

k = n

for _ in range(m):
    a, b = map(int,input().split())
    if union(a, b):
        k -= 1

answer = 0
if n > 1:
    answer = m - n + 2*k - 1
print(answer)
