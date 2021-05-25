# greedy
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = []
for i in a[::-1]:
    ans.append(k//i)
    k %= i
print(sum(ans))
