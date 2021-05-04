# 자료구조, 스택, 후위표기식
n = int(input())
l = input()
stack = []
alpha = [0]*n
for i in range(n):
    alpha[i] = int(input())
for j in l:
    if j.isalpha():
        stack.append(alpha[ord(j)-ord('A')])
    else:
        first = stack.pop()
        second = stack.pop()
        if j == '+':
            s = second + first
        elif j == '-':
            s = second - first
        elif j == '*':
            s = second * first
        elif j == '/':
            s = second / first
        stack.append(s)
print('%.2f' %stack[-1])
