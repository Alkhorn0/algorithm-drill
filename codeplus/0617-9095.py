# sw 역량 테스트 준비 - 기초 
def go(sum, goal):
    if sum > goal:
        return 0
    if sum == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(sum+i, goal)
    return now

T = int(input())
for _ in range(T):
    n = int(input())
    print(go(0, n))