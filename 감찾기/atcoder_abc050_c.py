n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7
check = [0]*(max(a)+1)
for i in a:
    check[i] += 1
for j in range(max(a)+1):
    if (check[j] > 2):
        print(0)
        exit()
    elif (n % 2 == 0) & (check[j] == 1):
        print(0)
        exit()
    elif (n % 2 == 1) & (check[0] > 1):
        print(0)
        exit()
        
a = set(a)
if n % 2 == 0:
    print(2**len(a)%mod)
else:
    print(2**(len(a)-1)%mod)