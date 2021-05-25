# greedy, sorting
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
m.sort(key=lambda x: x[0])
m.sort(key=lambda x: x[1])
ans = 1
s = m[0][1]
for i in range(1, n):
    if m[i][0] >= s:
        ans += 1
        s = m[i][1]
print(ans)
