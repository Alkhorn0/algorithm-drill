n = int(input())
l = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        l[i].append((x-1, y))
 
def check(k):
    for i in range(n):
        if k>>i & 1:
            for x, y in l[i]:
                if k>>x & 1 and y == 0:
                    return False
                if (not k>>x & 1) and y == 1:
                    return False
    return str(bin(k)).count('1')

ans = 0
for i in range(pow(2, n)):
    if check(i) > ans:
        ans = check(i)
print(ans)