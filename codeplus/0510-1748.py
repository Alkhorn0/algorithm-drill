# 틀림
n = int(input())
x = 0
ans = 0
for i in range(9):
    if n // 10**i < 10:
        x = i+1
        ans += (n-10**i+1)*3
        break
for j in range(1, x):
    ans += j*9*(10**(j-1))
print(ans)