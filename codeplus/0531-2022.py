import math
x, y, c = map(float, input().split())
left = 0
right = min(x, y)

while abs(right-left) > 1e-6:
    mid = (left+right)/2
    h1 = math.sqrt(x**2-mid**2)
    h2 = math.sqrt(y**2-mid**2)
    if c > (h1*h2)/(h1+h2):
        right = mid
    else:
        left = mid
print('%.3f'%left)