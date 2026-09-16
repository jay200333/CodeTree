N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# W, S, N, E
dy = [0, -1, 1, 0]
dx = [-1, 0, 0, 1]

def move():
    y, x = 0, 0
    answer = 0
    for i in range(N):
        if dir[i] == 'W':
            for i in range(1, dist[i]+1):
                y += dy[0]
                x += dx[0]
                answer += 1
                if y == 0 and x == 0:
                    return answer
        elif dir[i] == 'S':
            for i in range(1, dist[i]+1):
                y += dy[1]
                x += dx[1]
                answer += 1
                if y == 0 and x == 0:
                    return answer
        elif dir[i] == 'N':
            for i in range(1, dist[i]+1):
                y += dy[2]
                x += dx[2]
                answer += 1
                if y == 0 and x == 0:
                    return answer
        elif dir[i] == 'E':
            for i in range(1, dist[i]+1):
                y += dy[3]
                x += dx[3]
                answer += 1
                if y == 0 and x == 0:
                    return answer
    else:
        return -1
print(move())


