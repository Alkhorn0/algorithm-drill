result = []
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    elif v%p > l:
        result.append(l*(v//p)+l)
    else:
        result.append(l*(v//p)+v%p)

for i in range(len(result)):
    print(f"Case {i+1}:", result[i])

## 주의 v 시작부터 p카운팅할것 