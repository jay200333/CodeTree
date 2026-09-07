from collections import deque

dx = [-1, 1]
visited = [-1] * 1000001
N = int(input())
visited[N] = 0


def bfs():
    queue = deque([N])
    while queue:
        cur = queue.popleft()
        if cur == 1:
            return visited[1]
        next_node = []    
        if cur % 3 == 0:
            next_node.append(cur//3)
        elif cur % 2 == 0:
            next_node.append(cur//2)
        
        next_node.append(cur-1)
        next_node.append(cur+1)
        for nx in next_node:
            if nx < 0 or nx > 1000000: continue
            if visited[nx] == -1:
                visited[nx] = visited[cur] + 1
                queue.append(nx)

print(bfs())


    



# Please write your code here.
