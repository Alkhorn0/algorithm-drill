mod = 1000000007
n = int(input())
s1 = list(input())
s2 = list(input())

cnt = 0
ans = 1
patern = -1

while cnt < n:
    if s1[cnt] == s2[cnt]:
        if patern < 0:
            ans = 3
        elif patern == 0:
            ans *= 2
        else:
            ans *= 1
        cnt += 1
        patern = 0
    else:
        if patern < 0:
            ans = 6
        elif patern == 0:
            ans *= 2
        else:
            ans *= 3
        cnt += 2
        patern = 1
        
print(ans%mod)
            