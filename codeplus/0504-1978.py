# 수학, 소수
n = int(input())
l = list(map(int, input().split()))
prime = []
for i in l:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        prime.append(i)
print(len(prime))