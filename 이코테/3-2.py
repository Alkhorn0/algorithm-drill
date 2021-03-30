n, m, k = map(int, input().split(' '))
l = list(map(int, input().split(' ')))

l = sorted(l)

result = 0

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result += count * l[-1]         # 가장 큰 수 더하기
result += (m-count) * l[-2]     # 두 번째로 큰 수 더하기

print(result)