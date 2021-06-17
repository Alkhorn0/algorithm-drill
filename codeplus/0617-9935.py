# 다시보기
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