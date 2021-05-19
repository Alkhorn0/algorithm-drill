n = int(input())
s = list(map(int, input().split()))
check = [False]*(n*100000+10)
for i in range(1 << n):
    sum = 0
    for j in range(n):
        if (i & (1 << j)):
            sum += s[j]
    check[sum] = True

i = 1
while True:
    if check[i] == False:
        break
    i += 1
print(i)
