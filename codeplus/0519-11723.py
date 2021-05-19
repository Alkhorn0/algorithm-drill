import sys
n = 20
m = int(sys.stdin.readline())
s = 0
for _ in range(m):
    op, *num = sys.stdin.readline().split()
    if len(num) > 0:
        # 대입되는 수 중에 0이 없기 때문에 1을빼서 맞춰주는 듯
        x = int(num[0]) - 1
    # 부분집합 s에 원소 x를 추가 = add
    if op == 'add':
        s = (s | (1 << x))  # |(or) 활용

    # 부분집합 s에서 원소 x를 제거 = remove 
    elif op == 'remove':
        s = (s & ~(1 << x)) # ~(not)과 &(and)활용
    
    # 부분집합 s에서 원소 x가 존재하는지 판정 = check
    elif op == 'check':
        res = (s & (1 << x))    # &(and) 활용 있으면 res가 1 없으면 res 0
        if res > 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')

    # 부분집합 s에 x가 없으면 추가, 있으면 제거 = toggle
    elif op == 'toggle':
        s = (s ^ (1 << x))  # ^(xor) 활용
    
    # 1~20까지의 수를 s에 추가 = all
    elif op == 'all':
        s = (1 << n) - 1    # 이진수로 (1e20)2 에서 1빼면 1이 20개 있는 숫자 됨
    
    # s를 비우기 위해선 s를 0으로 함 = empty
    else:
        s = 0