import sys
input = sys.stdin.readline

a = list(input().rstrip())
t = input().rstrip()
a_reverse = list(reversed(a))
l = []
r = []
left = 0
right = len(t)-1
convert = True
length = len(a)
while left <= right:
    if convert:
        l.append(t[left])
        left += 1
        if l[-length:] == a:
            l[-length:] = []
            convert = False
    else:
        r.append(t[right])
        right -= 1
        if r[-length:] == a_reverse:
            r[-length:] = []
            convert = True
while r:
    l.append(r.pop())
    if l[-length:] == a:
        l[-length:] = []

print(''.join(l))