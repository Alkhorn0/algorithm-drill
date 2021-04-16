# 구현 문제
i = []
for _ in range(5):
    i.append(int(input()))
i.sort()
average = sum(i)//5
center = i[2]
print(average)
print(center)