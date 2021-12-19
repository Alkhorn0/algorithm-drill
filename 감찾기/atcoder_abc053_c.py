x = int(input())

cnt = x//11
left = x%11
ans = cnt*2

if left > 6:
    ans += 2
elif left > 0:
    ans += 1

print(ans)
