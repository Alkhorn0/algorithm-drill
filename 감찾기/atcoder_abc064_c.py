rate = [0]*9
def divide(ai):
    if ai < 400:
        rate[0] += 1
    elif ai < 800:
        rate[1] += 1
    elif ai < 1200:
        rate[2] += 1
    elif ai < 1600:
        rate[3] += 1
    elif ai < 2000:
        rate[4] += 1
    elif ai < 2400:
        rate[5] += 1
    elif ai < 2800:
        rate[6] += 1
    elif ai < 3200:
        rate[7] += 1
    else:
        rate[8] += 1
    return

n = int(input())
a = list(map(int, input().split()))
for ai in a:
    divide(ai)
ans1 = 0
for i in range(8):
    if rate[i] != 0:
        ans1 += 1

ans2 = ans1 + rate[8]

if ans1 == 0:
    ans1 += 1

print(ans1, ans2)