t = int(input())
a, b, c = 0, 0, 0 
if t % 10 != 0:
    print(-1)
else:
    for c in range(7):
        for b in range(6):
            for a in range(34):
                if t == 300*a + 60*b + 10*c:
                    print(a, b, c)
                    exit()
