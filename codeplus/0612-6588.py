# sw 역량 테스트 준비 - 기초
prime = [True]*1000001
prime[1] = False
for i in range(2, 1000001):
    if not prime[i]:
        continue
    j = 2
    while i*j <= 1000000:
        prime[i*j] = False
        j += 1
while True:
    n = int(input())
    if n == 0:
        break
    goldbach = False
    for i in range(2, n):
        if prime[i] == True and prime[n-i] == True:
            goldbach = True
            print(f'{n} = {i} + {n-i}')
            break
    if not goldbach:
        print("Goldbach's conjecture is wrong.")