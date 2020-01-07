# 39. Zipfの法則

# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

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
    morphemes = ma.get_all_morphemes()

    # 出現頻度と順位をとる
    words = ["{} {} {}".format(m["base"], m["pos"], m["pos1"]) for m in morphemes]
    word_count = Counter(words)
    frequencies = sorted(word_count.values(), reverse=True)
    rank = range(1, len(frequencies)+1)

    # 両対数グラフ描画
    plt.xscale("log")
    plt.yscale("log")
    plt.rcParams["font.family"] = "IPAexGothic"
    plt.xlabel("log 出現頻度順位")
    plt.ylabel("log 出現頻度")
    plt.plot(rank, frequencies)
    plt.show()
