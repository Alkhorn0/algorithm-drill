# greedy
# 묶어서 더하는 경우 가장 큰 수가 나오기 위해선,
# 1을 제외한 양수끼리의 곱, 음수끼리의 곱, 1의 갯수를 더해줄 필요가 있다
# 0의 경우는 합의 값이 음수를 더했을때 작아지는 것을 음수와 곱하여 0을 만들어 주는데 의의가 있다

import sys
input = sys.stdin.readline

n = int(input())
minus = []
plus = []
ans = 0
zero = 0
for _ in range(n):
    x = int(input())
    if x < 0:
        minus.append(x)
    elif x > 1:
        plus.append(x)
    # 1의 갯수 = 1을 더한 값
    elif x == 1:
        ans += 1
    else:
        zero += 1
# 음수의 경우 작은 수 일수록 절대값이 큰 수->
# 곱하면 큰 수 이므로 오름차순 정렬
minus.sort()
# 양수의 경우 큰 수부터 우선적으로 곱하기 위해서 내림차순 정렬
plus.sort(reverse=True)

# 계산시 편리함을 위해 리스트의 크기를 짝수로 만든다
if len(minus)%2 == 1:
    # 남은 음수는 0과 묶을 수 있으면 묶어준다
    if zero > 0:
        minus.pop()
    else:
        ans += minus.pop()
# 남는 양수는 그대로 더해주게 되는데 이 경우 
# 1을 곱한값과 같으므로 1을 추가해 전체 크기를 
# 짝수로 만든다
if len(plus)%2 == 1:
    plus.append(1)

for i in range(0, len(minus), 2):
    ans += (minus[i]*minus[i+1])

for i in range(0, len(plus), 2):
    ans += (plus[i]*plus[i+1])

print(ans)
