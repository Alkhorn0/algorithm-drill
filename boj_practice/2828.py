from sys import stdin

n, m = map(int, stdin.readline().split())
cnt = 0
basket_left = 1
basket_right = m
j = int(stdin.readline())
for __ in range(j):
    apple = int(stdin.readline())
    if apple < basket_left:
        cnt += (basket_left - apple)
        basket_left = apple
        basket_right = basket_left + m - 1
    elif apple > basket_right:
        cnt += (apple - basket_right)
        basket_right = apple
        basket_left = basket_right - m + 1
    else: continue
print(cnt)

