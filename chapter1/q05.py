# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# n-gram ???
# 任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法
# 「明日晴れるかな」　→　[明,日,晴,れ,る,か,な] unigram
# 「明日晴れるかな」　→　[明日,日晴,晴れ,れる,るか,かな] bigram

def get_n_gram(sequence, n:int) -> list:
    result = []
    for i in range(len(sequence)-n+1):
        result.append(sequence[i:i+n])
    
    return result

if __name__ == '__main__':
    # 単語bi-gram
    print(get_n_gram("I am an NLPer".split(), 2))
    # 文字bi-gram
    print(get_n_gram("I am an NLPer", 2))
