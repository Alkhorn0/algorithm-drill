t = []
for i in range(1,45):
    t_n = i*(i+1)/2
    t.append(t_n)

test_case = int(input())
for __ in range(test_case):
    k = int(input())
    for i in range(len(t)):
        if t[i] > k:
            border = i
            break
    cnt = 0
    for x in range(i):
        for y in range(i):
            for z in range(i):
                if k == t[x] + t[y] + t[z]:
                    cnt += 1

    if cnt != 0:
        print(1)
    else:
        print(0) 