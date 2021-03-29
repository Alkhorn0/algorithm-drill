n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n-i+1):
        k = n - i - j
        if (i*10000 + j*5000 + k*1000) == y and 0 <= k <= 2000:
            print(i, j, k)
            exit()

print(-1, -1, -1)   