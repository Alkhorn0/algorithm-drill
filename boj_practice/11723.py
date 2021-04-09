import sys

s = set()
n = int(sys.stdin.readline())

for i in range(n):
    commands = sys.stdin.readline().strip().split()

    if len(commnads) == 1:
        if commnads[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    command, x = commands[0], int(commands[1])

    if command == 'add':
        s.add(x)
    elif command == 'check':
        print(1 if x in s else 0)
    elif command == 'remove':
        s.discard(x)
    elif command == 'toggle':
        if x in s:
            s.discard(x)
        else:
            s.add(x)