x, y = map(int, input().split())
if x + y <= 1:
    print('Brown')
elif x + y > 1 and abs(x - y) <= 1:
    print('Brown')
elif x + y > 1 and abs(x - y) > 1:
    print('Alice')