a = list(input())
s = ''
ans = 1

for i in a:
    if i == 'c' and i != s:
        ans *= 26
    elif i == 'c' and i == s:
        ans *= 25
    elif i == 'd' and i != s:
        ans *= 10
    elif i == 'd' and i == s:
        ans *= 9
    s = i
print(ans)