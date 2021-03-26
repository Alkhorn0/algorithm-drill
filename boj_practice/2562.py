array = []
m = 0
for __ in range(9):
    n = int(input())
    array.append(n)

m = array[0]
n = 0
for i in range(1, 9):
    if m < array[i]:
        m = array[i]
        n = i

print(m)
print(n+1) 