n, r, c = map(int, input().split())

def go(n, r, c):
    if n == 1:
        return 2*r + c
    else:
        if r < 2**(n-1) and c < 2**(n-1):
            return go(n-1, r, c)
        elif r < 2**(n-1) and c >= 2**(n-1):
            return go(n-1, r, c-2**(n-1)) + 2**(2*n-2)
        elif r >= 2**(n-1) and c < 2**(n-1):
            return go(n-1, r-2**(n-1), c) + (2**(2*n-2))*2
        else:
            return go(n-1, r-2**(n-1), c-2**(n-1)) + (2**(2*n-2))*3

print(go(n, r, c))