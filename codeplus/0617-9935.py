# 다시보기
# 문자열 슬라이싱을 통해 파이썬은 쉽게 풀 수 있는 문제
# 변수 last에 폭발문자열의 마지막 문자를 저장 시키고, stack에 
# 입력문자열을 하나씩 추가하면서 last와 동일한 문자가 stack에 추가될 때,
# 폭발문자열의 크기만큼 역산하여 폭발 문자열이 포함되는지 확인 후 슬라이싱해준다.

import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
last = b[-1]
stack = []
length = len(b)

for i in a:
    stack.append(i)
    if i == last and ''.join(stack[-length:]) == b:
        del stack[-length:]
ans = ''.join(stack)

if ans == '':
    print('FRULA')
else:
    print(ans)