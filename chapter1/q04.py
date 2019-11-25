# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause.
#  Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
# 連想配列（辞書型もしくはマップ型）を作成せよ．

SENTENCE = r'Hi He Lied Because Boron Could Not Oxidize Fluorine.' + \
            r' New Nations Might Also Sign Peace Security Clause.' + \
            r' Arthur King Can.'
words = SENTENCE.split()
first_letter_from = [1, 5, 6, 7, 8, 9, 15, 16, 19]

result = dict()
for i,w in enumerate(words):
    if i+1 in first_letter_from:
        result[w[0]] = i+1
    else:
        result[w[0:2]] = i+1

print(result)
