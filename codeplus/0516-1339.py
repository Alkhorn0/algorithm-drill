# greedy, brute force, permutation
# 시간초과가 나옴 (python) -> 다시보기(다른 방법 알아보기)
def prev_permutation(a):
    i = len(a)-1
    while i>0 and a[i] >= a[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] >= a[i-1]:
        j -= 1
    a[j], a[i-1] = a[i-1], a[j]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
word = [list(input()) for _ in range(n)]
a = []
ans = 0
for i in range(n):
    for j in word[i]:
        if j not in a:
            a.append(j)
num = list(9-i for i in range(len(a)))
while True:
    pos = 0
    dict = {}
    for i in range(len(a)):
        dict[a[i]] = num[i]

    for j in range(n):
        for k in range(len(word[j])):
            pos += dict[word[j][k]]*10**(len(word[j])-1-k)
    if pos > ans:
        ans = pos
    if not prev_permutation(num):
        break
print(ans)
