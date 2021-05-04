# 문자열
# 여러줄 받을때는 sys.stdin.readlines사용
import sys
lines = sys.stdin.readlines()
for s in lines:
    lower, upper, number, space = 0, 0, 0, 0
    for i in s:
        x = ord(i)
        if ord('a') <= x <= ord('z'):
            lower += 1
        elif ord('A') <= x <= ord('Z'):
            upper += 1
        elif ord('0') <= x <= ord('9'):
            number += 1
        elif i == ' ':
            space += 1
    print(f'{lower} {upper} {number} {space}')
    