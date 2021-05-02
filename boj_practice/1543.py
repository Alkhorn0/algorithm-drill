# 그리디(?), 문자열
doc = input()
word = input()

result = doc.replace(word,'')
print((len(doc)-len(result))//len(word))

