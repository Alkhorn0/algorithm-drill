o = input()
e = input()

l_o = len(o)
l_e = len(e)

if l_o == l_e:
    ans = ''
    for i in range(l_o):
        ans += o[i]
        ans += e[i]
    print(ans)
else:
    ans = ''
    for j in range(l_e):
        ans += o[j]
        ans += e[j]
    ans += o[-1]
    print(ans)
