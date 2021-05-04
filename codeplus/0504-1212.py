# 수학, 진법관련
o = ["000", "001", "010", "011", "100", "101", "110", "111"]
s = input()
ans = ''
start = True
if s == '0':
    ans = '0'
for i in s:
    n = ord(i) - ord('0')
    if start and n < 4:
        if n == 0:
            continue
        elif n == 1:
            ans += '1'
        elif n == 2:
            ans += '10'
        elif n == 3:
            ans += '11'
        start = False
    else:
        ans += o[n]
        start = False
print(ans)