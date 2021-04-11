import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic, numbers = {}, {}
index = 1
for __ in range(n):
    pokemon = input().strip()
    dic[index] = pokemon
    numbers[pokemon] = index
    index += 1
for __ in range(m):
    search = input().strip()
    try:
        idx = int(search)
        print(dic[idx])
    except ValueError:
        print(numbers[search])