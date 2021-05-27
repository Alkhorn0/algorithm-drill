# greedy
# 가장 작은 수를 만들기 위해서는 음수를 많이 만들어야함
# '-'의 활용이 중요시됨, 기호를 저장하는 리스트와 
# 숫자를 저장하는 리스트를 따로 관리, 처음에는 숫자부터 나온다고 하니까
# 처음에는 숫자를 더해주기 위해 연산자배열에 1을 처음부터 추가해주고 시작

import sys
input = sys.stdin.readline

a = input().rstrip()
minus = False
# 나오는 숫자저장
num = []
# 나오는 연산자 저장
sign = [1]
cur = 0

for i in range(len(a)):
    # 덧셈과 뺄셈의 구분은 1과 -1로 한다
    if a[i] == '+' or a[i] == '-':
        if a[i] == '+':
            sign.append(1)
        else:
            sign.append(-1)
        # 연산자가 나오면 이전까지 저장된 숫자는 완성된 숫자이므로
        # 숫자배열에 저장해주고 다시 새로운 숫자를 받기위해 초기화
        num.append(cur)
        cur = 0
    # 숫자가 나오는 경우, 문자열로 입력을 받기때문에
    # 형변환 및 숫자로 바꿔야한다
    else:
        cur = cur*10 + int(a[i])
# 마지막으로 나온 숫자도 추가해준다
num.append(cur)
# 중첩해나갈 계산 결과
ans = 0
for i in range(len(num)):
    # '-'가 나온 이후의 '+'는 괄호안에서 더해지는 것으로 처리하므로
    # 일단 '-' 가 나온 이후의 연산은 빼기만 실행한다
    if sign[i] == -1:
        minus = True
    if minus:
        ans -= num[i]
    else:
        ans += num[i]

print(ans)