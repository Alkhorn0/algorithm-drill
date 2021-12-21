n, m = map(int, input().split())
if n == m//2:
    print(n)
elif n > m//2:
    print(m//2)
else:
    print((m-2*n)//4+n)