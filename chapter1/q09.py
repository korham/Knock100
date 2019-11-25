# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば"I couldn't believe that I could actually understand what I was reading :
#  the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

from random import sample

SAMPLE_SENTENCE = r"I couldn't believe that I could actually understand what I was reading :" + \
                    " the phenomenal power of the human mind ."

words = SAMPLE_SENTENCE.split()

def shuffle_middle_letter(word:str):
    if len(word) <= 4:
        return word
    else:
        middle = word[1:len(word)-1]
        shuffled = "".join(sample(middle,len(middle)))
        return word[0] + shuffled + word[len(word)-1]

print(" ".join(map(shuffle_middle_letter, words)))