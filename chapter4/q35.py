# 35. 名詞の連接

# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

import os
from mecabAnalysys import MecabAnalysys

if __name__ == "__main__":
    src = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")
    with open(src, encoding="utf-8") as f:
        ma = MecabAnalysys("\n".join(f.readlines()))
    ma.load()
    morph = ma.get_all_morphemes()

    noun_serieses = []
    is_going = False    # 名詞の連接を探している途中か
    noun_from = -1      # 連接はじめの名詞のindex
    noun_to = -1        # 連接おわりの名詞のindex
    for i,m in enumerate(morph):
        if m["pos"] == "名詞" and not is_going:
            # 連接チェックのはじまり
            noun_from = i
            noun_to = i
            is_going = True
        elif m["pos"] == "名詞" and is_going:
            # 名詞が連続していたらnoun_toを更新
            noun_to = i
        else:
            # 連接を探しているときに名詞以外が見つかったとき、はじめとおわりのindexが違えばそこまでが対象
            if is_going and noun_to > noun_from:
                print(noun_from, noun_to)
                series = [x["surface"] for x in morph[noun_from:noun_to+1]]
                noun_serieses.append("".join(series))
            is_going = False

    # 文末が名詞の連接だった場合の対応
    if is_going and noun_from != noun_to:
        series = [x["surface"] for x in morph[noun_from:noun_to]]
        noun_serieses.append("".join(series))
    
    output = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/q35.txt")
    with open(output, mode="w", encoding="utf-8") as f:
        f.write("\n".join(noun_serieses))
