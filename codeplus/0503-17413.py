# 자료구조, 스택
import sys
input = sys.stdin.readline
s = input()
stack = []
result = ''
switch = True
for i in s:
    if i == ' ' or i == '\n':
        while stack:
            result += stack.pop()
        result += i
    elif i == '<':
        switch = False
        while stack:
            result += stack.pop()
        result += i
    elif i == '>':
        switch = True
        result += i
    else:
        if switch == False:
            result += i
        else:
            stack.append(i)
print(result)
