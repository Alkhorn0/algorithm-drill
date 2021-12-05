w, h, n = map(int, input().split())
x_1, y_1 = 0, 0
x_2, y_2 = w, 0
x_3, y_3 = 0, 0
x_4, y_4 = 0, h

for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        x_1 = max(x_1, x)
    elif a == 2:
        x_2 = min(x_2, x)
    elif a == 3:
        y_3 = max(y_3, y)
    else:
        y_4 = min(y_4, y)

ans = (x_2-x_1)*(y_4-y_3) 
if x_2 <= x_1 or y_4 <= y_3:
    ans = 0
else:
    ans = (x_2-x_1)*(y_4-y_3) 
print(ans)