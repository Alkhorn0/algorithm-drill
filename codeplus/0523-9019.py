from collections import deque

def pri(a, b):
    if a == b:
        return
    pri(a, d[b])
    print(how[b], end='')

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    d = [-1]*10000
    how = ['']*10000
    d[a] = ''
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        nx = x*2 % 10000
        if d[nx] == -1:
            d[nx] = x
            how[nx] = 'D'
            q.append(nx)
            
        nx = x-1 if x > 0 else 9999
        if d[nx] == -1:
            d[nx] = x
            how[nx] = 'S'
            q.append(nx)

        nx = (x%1000)*10 + x//1000
        if d[nx] == -1:
            d[nx] = x
            how[nx] = 'L'
            q.append(nx)
            
        nx = (x//10) + (x%10)*1000
        if d[nx] == -1:
            d[nx] = x
            how[nx] = 'R'
            q.append(nx)
    pri(a, b)
    print()
