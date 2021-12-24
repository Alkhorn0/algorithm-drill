import math

n = int(input())

for i in range(int(math.sqrt(n)), 0, -1):
    if n % i == 0:
        x = n//i
        ans = 0
        while x > 0:
            ans += 1
            x //= 10
        print(ans)
        break
