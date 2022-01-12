A = [1, 3, 5, 7, 8, 10, 12]
B = [4, 6, 9, 11]
C = [2]

x, y = map(int, input().split())
if x in A:
    if y in A:
        print('Yes')
    else:
        print('No')
elif x in B:
    if y in B:
        print('Yes')
    else:
        print('No')
else:
    print('No')