def go(sum, goal):
    if sum > goal:
        return 0
    if sum == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(sum+i, goal)
    return now

t = int(input())
for _ in range(t):
    n = int(input())
    print(go(0, n))