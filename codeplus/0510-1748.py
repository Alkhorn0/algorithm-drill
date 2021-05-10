# 틀림
n = int(input())
ans = 0
for i in range(1, n+1):
    if i < 10:
        ans += 1
    elif i < 100:
        ans += 2
    elif i < 1000:
        ans += 3
    elif i < 10000:
        ans += 4
    elif i < 100000:
        ans += 5
    elif i < 1000000:
        ans += 6
    elif i < 10000000:
        ans += 7
    elif i < 100000000:
        ans += 8
    elif i < 1000000000:
        ans += 9
print(ans)