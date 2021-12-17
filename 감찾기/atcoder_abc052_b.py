n = int(input())
s = input()

ans = 0
x = 0

for i in s:
    if i == 'I':
        x += 1
    elif i == 'D':
        x -= 1
    ans = max(x, ans)
print(ans)