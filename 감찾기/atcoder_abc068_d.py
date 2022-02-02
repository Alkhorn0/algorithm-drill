k = int(input())

d, m = divmod(k, 50)
ans = [49+d]*50
for i in range(m):
    ans[i] += 1
for j in range(m, 50):
    ans[j] -= m

print(len(ans))
print(*ans)