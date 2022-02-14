a, b, c, d, e, f = map(int, input().split())

max_sugar_water = 10**9
max_sugar = 0
for i in range(0, f+1, 100*a):
    for j in range(0, f-i+1, 100*b):
        sugar_limit = (i+j)*e//100
        for k in range(0, sugar_limit+1, c):
            for l in range(0, sugar_limit-k+1, d):
                sugar = k + l
                water = i + j
                sugar_water = sugar + water
                if f < sugar_water:
                    continue
                if water == 0:
                    continue
                if max_sugar * sugar_water < sugar * max_sugar_water:
                    max_sugar = sugar
                    max_sugar_water = sugar_water

if max_sugar_water == 10**9:
    print(100*a, 0)
else:
    print(max_sugar_water, max_sugar)