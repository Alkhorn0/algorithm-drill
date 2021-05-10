n = int(input())
a = list(map(int, input().split()))
ans = [0]*(n+1)
for i in a:
    ans[i] += 1
for j in range(1, n+1):
    print(ans[j])