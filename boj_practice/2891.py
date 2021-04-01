n, s, r = map(int, input().split())
s_numbers = list(map(int, input().split()))
r_numbers = list(map(int, input().split()))


cnt = 0

for i in r_numbers:
    for j in s_numbers:
        if j == i+1 or j == i-1 or i == j:
            cnt += 1
            s_numbers.remove(j)
            break
print(s-cnt)