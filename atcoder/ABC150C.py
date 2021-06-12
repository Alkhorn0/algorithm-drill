n = int(input())
s = [i for i in range(1, n+1)]
P = -1
Q = -1
p = list(map(int, input().split()))
q = list(map(int, input().split()))
def next_permutation(s):
    i = len(s)-1
    while i > 0 and s[i] <= s[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(s)-1
    while s[j] <= s[i-1]:
        j -= 1
    s[i-1], s[j] = s[j], s[i-1]
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return True
cnt = 0 
if s == p:
    P = cnt
if s == q:
    Q = cnt
while (P == -1 or Q == -1) and (next_permutation(s)):
    cnt += 1
    if s == p:
        P = cnt
    if s == q:
        Q = cnt
print(abs(P-Q))
