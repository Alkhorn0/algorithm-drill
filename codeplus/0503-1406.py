# 다시 풀기
# 자료구조, 스택
import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
m = int(input())
for _ in range(m):
    line = input().rstrip().split()
    what = line[0]
    if what == 'L':
        if left:
            right.append(left.pop())
    elif what == 'D':
        if right:
            left.append(right.pop())
    elif what == 'P':
        left.append(line[1])
    elif what == 'B':
        if left:
            left.pop()
left += right[::-1]
print(''.join(left))