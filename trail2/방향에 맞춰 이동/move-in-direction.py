n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dy = [-1, 0, 1, 0]
dx = [0, -1 ,0, 1]

# Please write your code here.
answer = [0, 0]
for i in range(n):
    if dir[i] == 'S':
        answer[1] += dx[0] * dist[i]
        answer[0] += dy[0] * dist[i]
        
    elif dir[i] == 'N':
        answer[1] += dx[2] * dist[i]
        answer[0] += dy[2] * dist[i]
    elif dir[i] == 'W':
        answer[1] += dx[1] * dist[i]
        answer[0] += dy[1] * dist[i]
    else:
        answer[1] += dx[3] * dist[i]
        answer[0] += dy[3] * dist[i]

print(answer[1], answer[0])
