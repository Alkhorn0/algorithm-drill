def action(t, a, b):
    if t == 3:
        print('Yes' if (a, b) in g and (b, a) in g else 'No')
    elif t == 1:
        g.add((a, b))
    else:
        g.discard((a, b))
    return 

n, q = map(int, input().split())
g = set()
for _ in range(q):
    t, a, b = map(int, input().split())
    action(t, a, b)
    #print(g)