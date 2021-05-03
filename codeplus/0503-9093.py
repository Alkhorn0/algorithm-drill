# 자료구조
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    stack = [' ']
    sentence = input().rstrip()
    result = ''
    for i in sentence:
        if i == ' ':
            while stack:
                result += stack.pop()
        stack.append(i)
    while stack:
        result += stack.pop()
    print(result)

