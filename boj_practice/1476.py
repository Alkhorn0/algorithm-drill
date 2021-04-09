e, s, m = map(int, input().split())
n = 1
while True:
    j_e = n % 15
    if j_e == 0:
        j_e = 15
    j_s = n % 28
    if j_s == 0:
        j_s = 28
    j_m = n % 19
    if j_m == 0:
        j_m = 19
    if j_e == e and j_s == s and j_m == m:
        break
    n += 1

print(n)