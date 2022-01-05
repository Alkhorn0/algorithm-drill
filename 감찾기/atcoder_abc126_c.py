n, k = map(int, input().split())
ans = 0

for i in range(1, n+1):
    score = i
    i_per = 1/n
    while score < k:
        score *= 2
        i_per *= 0.5
    ans += i_per

print(ans)
