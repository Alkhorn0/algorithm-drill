n = int(input())
s = [input() for _ in range(n)]
table = list(list(0 for _ in range(26)) for _ in range(n))

for i in range(n):
    for c in s[i]:  
        table[i][ord(c)-ord('a')] += 1

ans = ''
for x in range(26):
    check = True
    cnt = 100
    alpha = chr(x+ord('a'))
    for y in range(n):
        if table[y][x] == 0:
            check = False
        cnt = min(table[y][x], cnt)
    if check:
        ans += (alpha*cnt)
print(ans)