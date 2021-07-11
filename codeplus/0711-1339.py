# sw 역량 테스트 준비 - 기초 
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def calc(a, word, d):
    l = len(word)
    ans = 0
    alphabet = dict()
    for i in range(l):
        alphabet[word[i]] = d[i]
    for j in a:
        now = 0
        for x in j:
            now = now*10 + alphabet[x]
        ans += now
    return ans

n = int(input())
a = ['']*n
word = set()
for i in range(n):
    a[i] = input()
    word |= set(a[i])
word = list(word)
l = len(word)
d = [i for i in range(9, 9-l, -1)]
d.sort()
ans = 0
while True:
    now = calc(a, word, d)
    if ans < now:
        ans = now
    if not next_permutation(d):
        break
print(ans)