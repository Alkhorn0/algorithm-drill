a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0

for i in range(c + 1):
    for j in range(b + 1):
        for k in range(a + 1):
            if x == 500*k + 100*j + 50*i:
                cnt += 1
                

print(cnt)