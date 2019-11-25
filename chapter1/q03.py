# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

SENTENCE = r'Now I need a drink, alcoholic of course,' + \
            r' after the heavy lectures involving quantum mechanics.'

fixed_sentence = ''
for char in SENTENCE:
    if char == ' ' or char.isalpha():
        fixed_sentence += char

words = fixed_sentence.split()   
result = [len(x) for x in words]

print(result)