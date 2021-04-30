# 구현
T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    if n == 0:
        arr = input()
        arr = []
    else:
        arr = list(map(int, input()[1:-1].split(',')))
    r = False
    toggle = True
    front = 0
    rear = 0

    for i in p:
        try:
            if i == 'R':
                r = not r
            elif i == 'D' and not r:
                front += 1
            elif i == 'D' and r:
                rear += 1
        except:
            toggle = False
            print('error')
            break
    
    if toggle:
        if front + rear <= n:
            if not r:
                arr = arr[front: n-rear]
                print(str(arr).replace(' ',''))
            else:
                arr = arr[::-1][rear: n-front]
                print(str(arr).replace(' ',''))
        else:
            print('error')