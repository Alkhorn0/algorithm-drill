# 수학, 소수, 에라토스테네스의 체
MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] = True

for i in range(2, MAX+1):
    if not check[i]:
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i

T = int(input())
for _ in range(T):
    n = int(input())
    ans = 0
    for i in range(n//2+1):
        if check[i] == False and check[n-i] == False:
           ans += 1 
    print(ans)