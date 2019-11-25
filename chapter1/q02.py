# 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

STRING_1 = 'パトカー'
STRING_2 = 'タクシー'

result = ''
for c1,c2 in zip(STRING_1, STRING_2):
    result += (c1 + c2)

print(result)