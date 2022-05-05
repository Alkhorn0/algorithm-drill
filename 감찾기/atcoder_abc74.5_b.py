from collections import defaultdict


n = int(input())
ab = defaultdict()
for _ in range(n):
    ai, bi = map(int, input().split())
    ab[ai] = bi
m_k = min(ab, key=ab.get)
m_v = ab[m_k]
print(m_k+m_v)
