a, b, c = map(int, input().split())

m = (a if a < b else b) if ((a if a < b else b)< c) else c
print(m)