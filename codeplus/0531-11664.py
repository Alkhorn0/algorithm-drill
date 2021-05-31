import math

ax,ay,az,bx,by,bz,cx,cy,cz = map(int, input().split())
l1 = math.sqrt((ax-cx)**2+(ay-cy)**2+(az-cz)**2)
l2 = math.sqrt((bx-cx)**2+(by-cy)**2+(bz-cz)**2)
left = 0
right = 1
m = 0
dx = bx-ax
dy = by-ay
dz = bz-az

while True:
    if abs(right-left)<1e-9:
        m = (left+right)/2
        break
    m1 = left + (right-left)/3
    m2 = right - (right-left)/3
    m1x = ax + m1*dx
    m1y = ay + m1*dy
    m1z = az + m1*dz
    m2x = ax + m2*dx
    m2y = ay + m2*dy
    m2z = az + m2*dz
    d1 = math.sqrt((m1x-cx)**2+(m1y-cy)**2+(m1z-cz)**2)
    d2 = math.sqrt((m2x-cx)**2+(m2y-cy)**2+(m2z-cz)**2)
    if d1 > d2:
        left = m1
    else:
        right = m2
ansx = ax + m*dx
ansy = ay + m*dy
ansz = az + m*dz
ans = math.sqrt((ansx-cx)**2+(ansy-cy)**2+(ansz-cz)**2)
print('%.10f'%ans)