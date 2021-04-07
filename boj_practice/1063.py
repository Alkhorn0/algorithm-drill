dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

king, stone, n = map(str, input().split())

king_pos = [alpha.index(king[0]), int(king[1])]
stone_pos = [alpha.index(stone[0]), int(stone[1])]

for __ in range(int(n)):
    idx = move.index(input())
    nx = king_pos[0] + dx[idx]
    ny = king_pos[1] + dy[idx]

    if nx < 0 or ny < 1 or nx > 7 or ny > 8:
        continue

    if nx == stone_pos[0] and ny == stone_pos[1]:
        px = stone_pos[0] + dx[idx]
        py = stone_pos[1] + dy[idx]

        if px < 0 or py < 1 or px > 7 or py > 8:
            continue
        stone_pos[0] = px
        stone_pos[1] = py
    
    king_pos[0] = nx
    king_pos[1] = ny

king_result = alpha[king_pos[0]] + str(king_pos[1])
stone_result = alpha[stone_pos[0]] + str(stone_pos[1]) 

print(king_result)
print(stone_result)