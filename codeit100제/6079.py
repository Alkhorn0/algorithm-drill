n = int(input())
i = 1
s = 0
while True:
    s += i
    if s >= n:
        print(i)
        break
    i += 1