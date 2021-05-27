# greedy
# 30의 배수 -> 2,3,5의 배수 -> 1의자리수 = 0 & 전체 자리수의 합 = 3의 배수
# 이를 지키면서 가장 큰 수 -> 숫자를 내림차순 정렬하면 0이 제일 뒤로감(1의 자리) & 최대수
# 각 자리수를 합해 3의 배수인지 판별 하여 나타냄
n = sorted(list(map(int, list(input()))),reverse=True)
s = 0
for i in n:
    s += i
if s % 3 != 0 or 0 not in n:
    print(-1)
else:
    print(''.join(map(str, n)))