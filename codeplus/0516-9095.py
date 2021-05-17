# brute force, recursive
def go(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    ans = 0
    for i in range(1, 4):
        ans += go(n-i)
    return ans

T = int(input())
for _ in range(T):
    n = int(input())
    print(go(n))