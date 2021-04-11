alpha = 'abcdefgh'
location = input()
hor = 0
for i in alpha:
    hor += 1
    if i == location[0]:
        break
ver = int(location[1])
move_x = [-1, 1, -2, -2, -1, 1, 2, 2]
move_y = [2, 2, -1, 1, -2, -2, 1, -1]
answer = 0
for i in range(8):
    dx = hor + move_x[i]
    dy = ver + move_y[i]
    if 1 <= dx <= 8 and 1<= dy <=8:
        answer += 1

print(answer)