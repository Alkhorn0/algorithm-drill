import sys
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dic = dict()

for i in cards:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
        
for i in numbers:
    try:
        print(dic[i], end=" ")
    except:
        print(0, end=" ")