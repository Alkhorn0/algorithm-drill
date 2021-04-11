# 해싱문제 
l = int(input())
q = input()
answer = 0
for i in range(l):
    answer += (ord(q[i]) - 96)*(31**i)
print(answer % 1234567891)

