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

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(3, MAX):
            if check[i] != True and check[n-i] != True:
                print(f'{n} = {i} + {n-i}')
                break
            else:
                if i == MAX-1:
                    print("Goldbach's conjecture is wrong.")