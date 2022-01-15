n = int(input())
S = input()
s = list(S)
l, r = 0, 0
for _ in range(n):
    i = s.pop()
    if i == ')':
        l += 1
    else:
        if l > 0:
            l -= 1
        else:
            r += 1

ans = '('*l + S + ')'*r
print(ans)