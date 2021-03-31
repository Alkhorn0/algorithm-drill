result = []
while True:
    l = list(map(int, input().split()))
    n = l[0]
    if n == 0:
        break
    else:
        l.remove(n)
        l = sorted(l)
        a, b = 0, 0
        if n % 2 != 0:
            if 0 not in l:
                for i in range(0,n//2+1):
                    a +=l[2*i]*(10**(n//2-i))
                for j in range(0,n//2):
                    b +=l[2*j+1]*(10**(n//2-j-1))
                result.append(a + b)
            else:
                cnt = 0
                for k in l:
                    if k == 0:
                        cnt += 1
                a = l[cnt] *(10**(n//2))
                b = l[cnt + 1]*(10**(n//2-1))
                for i in range((cnt+2),n,2):
                    a +=l[i]*(10**((n-i-1)//2))
                for j in range((cnt+2)+1,n,2):
                    b +=l[j]*(10**((n-j-1)//2))
                result.append(a+b)
        
        else:
            if 0 not in l:
                for i in range(0,n//2):
                    a +=l[2*i]*(10**(n//2-i-1))
                for j in range(0,n//2):
                    b +=l[2*j+1]*(10**(n//2-j-1))
                result.append(a + b)
            else:
                cnt = 0
                for k in l:
                    if k == 0:
                        cnt += 1
                a = l[cnt] *(10**(n//2-1))
                b = l[cnt + 1]*(10**(n//2-1))
                for i in range((cnt+2),n,2):
                    a +=l[i]*(10**((n-i-1)//2))
                for j in range((cnt+2)+1,n,2):
                    b +=l[j]*(10**((n-j-1)//2))
                print(a,b)
                result.append(a+b)

for i in result:
    print(i)