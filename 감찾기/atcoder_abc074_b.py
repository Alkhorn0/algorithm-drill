n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += 2*min(x[i], abs(k-x[i]))
print(ans)