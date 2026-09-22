board = [list(map(int, input().split())) for _ in range(19)]

def omock():
    for i in range(19):
        for j in range(19):
            color = board[i][j]
            if color == 0:
                continue

            if 0 <= i - 2 and i + 2 < 19:
                if board[i-2][j] == color and board[i-1][j] == color and board[i+1][j] == color and board[i+2][j] == color:
                    return color, i, j

            if 0 <= j - 2 and j + 2 < 19:
                if board[i][j-2] == color and board[i][j-1] == color and board[i][j+1] == color and board[i][j+2] == color:
                    return color, i, j

            if 0 <= i - 2 and i + 2 < 19 and 0 <= j - 2 and j + 2 < 19:
                if board[i-2][j-2] == color and board[i-1][j-1] == color and board[i+1][j+1] == color and board[i+2][j+2] == color:
                    return color, i, j

            if 0 <= i - 2 and i + 2 < 19 and 0 <= j - 2 and j + 2 < 19:
                if board[i+2][j-2] == color and board[i+1][j-1] == color and board[i-1][j+1] == color and board[i-2][j+2] == color:
                    return color, i, j

    return 0, 0, 0

result = omock()

print(result[0])
if result[0] != 0:
    print(result[1] + 1, result[2] + 1)

        
