T = int(input())

for __ in range(T):
    r,s = input().split()
    for i in s:
        print(int(r)*i,end='')
    print()
