# 수학, 소수, 에라토스테네스의 체
MAX = 10000000
check = [0]*(MAX+1)
check[0] = check[1] = True

for i in range(2, MAX+1):
    if not check[i]:
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i

n = int(input())
k = 2
while n > 1:
    if not check[k] and n % k == 0:
        print(k)
        n //= k
    else:
        k += 1 
