n, k = map(int, input().split())
people = [0]*(n+1)
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for i in a:
        people[i] += 1

ans = 0
for i in people:
    if i == 0:
        ans += 1
print(ans-1)