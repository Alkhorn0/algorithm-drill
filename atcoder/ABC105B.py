def judge(n):
    for i in range(14):
        for j in range(25):
            if i*7 + j*4 == n:
                return True
    return False

n = int(input())

if judge(n):
    print('Yes')
else:
    print('No')