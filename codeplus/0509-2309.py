# 브루트포스
dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
dwarf = sorted(dwarf)
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if sum(dwarf)-(dwarf[i]+dwarf[j]) == 100:
            for k in dwarf:
                if k != dwarf[i] and k != dwarf[j]:
                    print(k)
            exit()
