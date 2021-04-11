# 스택문제 
n = int(input())
stack = []
result = []
count = 0
possible = True

for __ in range(n):
    num = int(input())

    while count < num:
        count += 1
        stack.append(count)
        result.append("+")
    
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break
if possible == False:
    print("NO")
else:
    for i in result:
        print(i)