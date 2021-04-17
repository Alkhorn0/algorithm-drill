T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    dictionary = {}     # 딕셔너리

    for i in str1:
        dictionary[i] = str2.count(i)
    print(f'#{t} {max(dictionary.values())}')