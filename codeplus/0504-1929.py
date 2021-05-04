# 수학, 소수,에라토스테네스의 체
# 다시보기
MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] = True

for i in range(2, MAX+1):
    if not check[i]:
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i

m, n = map(int, input().split())
for i in range(m, n+1):
    if check[i] == False:
        print(i)