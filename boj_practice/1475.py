room_number = input()
set = [0 for i in range(10)]

for i in room_number:
    i = int(i)
    for j in range(10):
        if j == i:
            set[j] += 1

if set[6] != set[9]:
    gap = abs(set[6]-set[9])//2
    if set[6] > set[9]:
        set[6] -= gap
    else:
        set[9] -= gap
    

max_set = set[0]
for i in range(9):
    if max_set  < set[i+1]:
        max_set = set[i+1]

print(max_set)

