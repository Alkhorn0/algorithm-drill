str1 = input()
str2 = input()
m = len(str1)
n = len(str2)

def BruteForce(str1, str2):
    i = 0
    j = 0
    while j < m and i < n:
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == m: return 1
    else: return 0

print(BruteForce(str1, str2))
            