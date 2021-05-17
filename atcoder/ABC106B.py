n = int(input())
odd = [i for i in range(n+1) if i % 2 == 1]
ans = 0
for j in odd:
  cnt = 0
  for k in odd:
    if j % k == 0:
      cnt += 1
  if cnt == 8:
    ans += 1
print(ans)