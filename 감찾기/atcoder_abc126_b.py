s = input()
a = s[:2]
b = s[2:]

if 1<=int(a)<=12:
    if 1<=int(b)<=12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if 1<=int(b)<=12:
        print('YYMM')
    else:
        print('NA')