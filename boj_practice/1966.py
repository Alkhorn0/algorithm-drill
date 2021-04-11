t = int(input())
for __ in range(t):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))
    idx = list(range(len(doc)))
    idx[m] = 'target'

    cnt = 0

    while True:
        if doc[0] == max(doc):
            cnt += 1
            if idx[0] == 'target':
                print(cnt)
                break
            else:
                doc.pop(0)
                idx.pop(0)
        else:
            doc.append(doc.pop(0))
            idx.append(idx.pop(0))
