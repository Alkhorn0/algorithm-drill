s = []
dvd_not10 = []
n = int(input())
for _ in range(n):
    si = int(input())
    s.append(si)
    if si % 10 != 0:
        dvd_not10.append(si)

max_score = sum(s)
final_score = 0 if max_score % 10 == 0 else max_score
if final_score == 0:
    if dvd_not10:
        dvd_not10 = sorted(dvd_not10)
        final_score = max_score - dvd_not10[0]

print(final_score)