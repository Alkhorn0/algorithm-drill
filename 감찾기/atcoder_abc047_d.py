n, t = map(int, input().split())
a = list(map(int, input().split()))
income = {}
m = max(a)

for i in a:
    if m > i:
        m = i
    else:
        if i-m in income:
            income[i-m] += 1
        else:
            income[i-m] = 1

print(income[max(income)])