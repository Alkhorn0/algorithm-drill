n = int(input())
ans = 0
cnt = -1

for i in range(1, n+1):
    j = i
    cnt_i = 0
    while j % 2 == 0:
        j //= 2
        cnt_i += 1
    if cnt < cnt_i:
        ans = i
        cnt = cnt_i
print(ans)