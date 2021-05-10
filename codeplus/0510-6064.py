# 브루트포스
def uclid(i, j):
    if j == 0:
        return i
    else:
        return uclid(j, i%j)
T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    l = m*n//uclid(m, n)
    ans = -1
    i = 0
    while m*i+x <= l:
        if (m*i+x)%n == y or ((m*i+x)%n == 0 and y == n):
            ans = m*i+x
            break
        i += 1
    print(ans)