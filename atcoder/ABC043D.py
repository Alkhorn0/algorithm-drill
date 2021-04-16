'''
연속하는 문자열에서 특정문자가 과반수로 
나오는 문자열 판정
'''
s = list(input())
n = len(s)
if n == 2 and s[0] == s[1]:  # 문자열 길이가 2인데 같은 문자일때
    print("1 2")
    exit()
for i in range(n-2):    
    if s[i] == s[i+1]:      # 같은 문자가 연달아 나올때는 무조건 해당
        print("{0} {1}".format(i+1, i+2))
        exit()
    if s[i] == s[i+2]:      # 문자열의 길이는 중요하지 않았으니 최대한 짧게 가면 됨 
        print("{0} {1}".format(i+1, i+3))
        exit()
print("-1 -1")      # 아무것도 해당 안될때