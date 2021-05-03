# 자료구조, 스택
import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
save = 1
for _ in range(n):
    integer = int(input())
    if len(stack) == 0:
        for i in range(save, integer+1):
            stack.append(i)
            result.append('+')
        save = integer + 1
    if stack[-1] < integer:
        for i in range(save, integer+1):
            stack.append(i)
            result.append('+')
        save = integer + 1
        stack.pop()
        result.append('-')
    elif integer == stack[-1]:
        stack.pop()
        result.append('-')

if stack:
    print('NO')
else:
    for i in result:
        print(i)