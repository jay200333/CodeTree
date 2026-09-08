n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
blocks = [[[1,0],[1,1]], [[1,1,1]]]

def turn(block):
    turned_block = [[0] * len(block) for _ in range(len(block[0]))]
    for i in range(len(block)):
        for j in range(len(block[0])):
            turned_block[j][len(block) - i - 1] = block[i][j]
    return turned_block

def reflect(block):
    return [row[::-1] for row in block]

def calculate(block):
    w = len(block)
    h = len(block[0])
    result = 0
    for i in range(n - w + 1):
        for j in range(m - h + 1):
            temp = 0
            for k in range(w):
                for l in range(h):
                    if block[k][l]:
                        temp += grid[i+k][j+l]
            result = max(result, temp)
    return result

answer = 0
for i in range(len(blocks)):
    block = blocks[i]
    for block in (block, reflect(block)):
        for j in range(4):
            block = turn(block)
            answer = max(answer, calculate(block))
print(answer)

