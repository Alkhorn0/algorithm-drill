T = int(input())
for t in range(1, T+1):
    forth = ['+','-','*','/']
    equation = list(input().split())
    stack = []
    for i in equation:
        if i not in forth and i != '.':
            stack.append(int(i))
        elif i in forth:
            try:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                else:
                    stack.append(a//b)
            except:
                print(f'#{t} error')
                break
        else:
            if len(stack) == 1:
                print(f'#{t} {stack[-1]}')
            else:
                print(f'#{t} error')
