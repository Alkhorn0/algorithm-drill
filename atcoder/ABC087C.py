n = int(input())
a_1 = list(map(int, input().split()))
a_2 = list(map(int, input().split()))

if n == 1:
    print(a_1[0]+a_2[0])
else:
    max_possible = 0
    possible = 0
    for i in range(n-1,-1,-1):
        possible += a_2[i]
        new = a_1[0:i+1]
        possible += sum(new)
        max_possible = max(possible, max_possible)
        possible -= sum(new)
    print(max_possible)
        