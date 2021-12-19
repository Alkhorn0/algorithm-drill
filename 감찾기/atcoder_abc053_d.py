n = int(input())
a = set(list(map(int, input().split())))
k = len(a)

if k%2 == 0:
    print(k-1)
else:
    print(k)