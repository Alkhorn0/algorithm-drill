s = input()
a = 1 if s[0] == 'H' else 0
b = 1 if s[-1] == 'H' else 0

print('D' if a^b else 'H')