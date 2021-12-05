n = int(input())
s = int(input())

if s > n:
    print(-1)   # b < 1 이라는게 됨
    exit()
elif s == n:
    print(n + 1)    # s=n이되려면 b > n이고, 이때의 최소값은 n+1
    exit()
    
# b-1 = (n-s)/p 값 구하기 
g = n - s
div_list = []
for i in range(1, int(g**0.5+1)):
    if g % i == 0:
        div_list.append(i)
        div_list.append(g//i)
        if i == g//i:
            div_list.pop()

div_list.sort()

def calc(b, n):
    if n < b:
        return n
    else:
        return calc(b, n // b) + (n % b)

for b in div_list:
    if calc(b + 1, n) == s:
        print(b+1)
        exit()
print(-1)