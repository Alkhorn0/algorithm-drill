n = int(input())
o_t, o_x, o_y = 0, 0, 0
judge = 0

for __ in range(n):
    t, x, y = map(int, input().split(' '))
    if ((t-o_t) >= abs(x-o_x)+abs(y-o_y)) and (t % 2 == (x+y) % 2):
        judge += 1
    o_t, o_x, o_y = t, x, y
print("Yes" if judge == n else "No")
        

