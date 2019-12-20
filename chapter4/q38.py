# 38. ヒストグラム

# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

import os
from collections import Counter
from operator import itemgetter
from matplotlib import pyplot as plt
from mecabAnalysys import MecabAnalysys

if __name__ == "__main__":
    src = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")
    with open(src, encoding="utf-8") as f:
        ma = MecabAnalysys("\n".join(f.readlines()))
    ma.load()
    morph = ma.get_all_morphemes()

    # 出現頻度を抽出
    words = ["{} {} {}".format(m["base"], m["pos"], m["pos1"]) for m in morph]
    word_count = Counter(words)
    frequencies = word_count.values()

    # ヒストグラム描画
    plt.hist(frequencies, 20, (0,50))
    plt.rcParams["font.family"] = "IPAexGothic"
    plt.xlabel("出現頻度")
    plt.ylabel("単語の種類")
    plt.show()
