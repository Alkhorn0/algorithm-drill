n = int(input())
insert = []
for __ in range(n):
    word = input()
    if word in insert:
        continue
    insert.append(word)

sort = sorted(sorted(insert), key=len)

for i in sort:
    print(i)