# 재귀 문제
def z(n, r, c):
    global cnt
    if n == 0:
        return cnt
    else:
        if r < 2**(n-1) and c < 2**(n-1):
            cnt += 0
            z(n-1, r%(2**(n-1)), c%(2**(n-1)))
        elif r < 2**(n-1) and c >= 2**(n-1):
            cnt += 4**(n-1)
            z(n-1, r%(2**(n-1)), c%(2**(n-1)))
        elif r >= 2**(n-1) and c < 2**(n-1):
            cnt += 2*(4**(n-1))
            z(n-1, r%(2**(n-1)), c%(2**(n-1)))
        else:
            cnt += 3*(4**(n-1))
            z(n-1, r%(2**(n-1)), c%(2**(n-1)))


n, r, c = map(int, input().split())
cnt = 0
z(n, r, c)
print(cnt)
