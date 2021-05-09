# 브루트포스
e, s, m = map(int, input().split())
x = 1
while True:
    e_x = x % 15
    s_x = x % 28
    m_x = x % 19
    if e_x == 0:
        e_x = 15
    if s_x == 0:
        s_x = 28
    if m_x == 0:
        m_x = 19
    if e_x == e and s_x == s and m_x == m:
        break
    x += 1
print(x)