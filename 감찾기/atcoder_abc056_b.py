w, a, b = map(int, input().split())

m, M = min(a, b), max(a, b)

print(M-(m+w) if M-(m+w) >= 0 else 0)