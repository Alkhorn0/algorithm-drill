# 자료구조, 덱
import sys
input = sys.stdin.readline

n = int(input().strip())
deque = []
for _ in range(n):
    command = list(input().strip().split())
    if command[0] == 'push_front':
        tmp = [command[1]]
        deque = tmp + deque
    elif command[0] == 'push_back':
        deque.append(command[1])
    elif command[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)